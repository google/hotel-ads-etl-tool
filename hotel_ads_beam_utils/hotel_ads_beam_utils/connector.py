# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from datetime import datetime
from datetime import timedelta

import os
import re
import tempfile

from .login import HotelAdsApiLogin

import requests
import gc

from google.cloud import storage


class HotelAdsApiConnector(object):
  """Main class of the Hotel Ads Api Connector in charge of data collection."""

  URL_AUTH = 'https://www.googleapis.com/auth/travelpartner'
  URL_REPORT = 'https://www.googleapis.com/travelpartner/v2.1/{0}/reports'
  CHUNK_SIZE = 64 * 1024 * 1024

  def __init__(self, account_id, bucket_name,
               key_file, partner_name):
    self.account_id = account_id
    self.bucket_name = bucket_name
    self.key_file = key_file
    self.partner_name = partner_name

    self.main_url = self.URL_REPORT.format(self.account_id)

    self._counter = 0


  def run(self, filename, report_date):
    if report_date is None:
      self.allowed_dates = [(datetime.today() - timedelta(2)).strftime('%Y%m%d')]
    else:
      self.allowed_dates = [report_date]

    self.cs_filename = filename

    self.login()

    fd, self.tmppath = tempfile.mkstemp()
    self.tmpfile = os.fdopen(fd, 'w')

    self.get_all_reports()

    self.tmpfile.flush()
    os.fsync(self.tmpfile)

    self.send_to_cs()

    self.tmpfile.close()
    os.remove(self.tmppath)

  def login(self):
    api = HotelAdsApiLogin(self.account_id, self.key_file, self.partner_name)
    api.initialize_credentials(self.URL_AUTH)
    self.bearer_token = api.get_connection_token()
    self.headers = {'Authorization': 'Bearer {0}'.format(self.bearer_token)}

  def get_all_reports(self):
    """Gets all the reports for the specified date."""

    print('Requesting list of report types...')
    url = self.main_url
    print('url: {}'.format(url))
    response = requests.get(url, headers=self.headers)
    if response.status_code != 200:
      raise ValueError(
          'The url [{0}] didn\'t respond properly. Response status: [{1}]'.
          format(url, response.status_code))
    json_data = response.json()
    report_types = json_data['report_types']
    for report_type in report_types:
      self.get_report(report_type)

  def get_report(self, report_name):
    """Gets a specific report for the specified date."""

    url = '{0}/{1}'.format(self.main_url, report_name)
    print('Requesting list of dates for report [{0}]...'.format(report_name))
    response = requests.get(url, headers=self.headers)
    if response.status_code == 204:
      print('no content')
      return
    if response.status_code != 200:
      raise ValueError(
          'The url [{0}] didn\'t respond properly. Response status: [{1}]'.
          format(url, response.status_code))
    json_data = response.json()
    dates = json_data['dates']
    for report_date in dates:
      if report_date in self.allowed_dates:
        print(' - {0}'.format(report_date))
        url = '{0}/{1}/{2}'.format(self.main_url, report_name, report_date)
        print(' Requesting report [{0}/{1}]...'.format(report_name,
                                                       report_date))
        is_first = True
        nextrow = None
        while is_first or nextrow is not None:
          is_first = False
          if nextrow is not None:
            nextrow_url = '{0}?nextrow={1}'.format(url, nextrow)
            print(' Requesting nextrow {}'.format(nextrow))
          else:
            nextrow_url = url
          response = requests.get(nextrow_url, headers=self.headers)

          print(' --- Status: [{}]'.format(response.status_code))
          if response.status_code in [204, 404]:
            print('--- no content')
            continue
          if response.status_code != 200:
            raise ValueError(
                'The url [{0}] didn\'t respond properly. Response status [{1}]'
                .format(url, response.status_code))
          entries = response.text.splitlines()
          first_row = entries.pop(0)
          nextrow_search = re.search('NEXTROW: (.+)', first_row, re.IGNORECASE)

          if nextrow_search:
            _ = entries.pop(0)
            nextrow = nextrow_search.group(1)
          else:
            nextrow = None

          ids = list(range(self._counter, self._counter + len(entries)))
          types = [report_name] * len(entries)
          dates = [report_date] * len(entries)

          for entry in entries:
            line = '{0},{1},{2},{3}'.format(
                self._counter,
                report_name,
                report_date,
                entry.encode('utf-8'))
            self.tmpfile.write('{}\n'.format(line))
            self._counter += 1
          print(' --- Total items so far: {0}'.format(self._counter))

          entries = None
          gc.collect()

  def send_to_cs(self):
    """Dumps all entries to a blob in CS."""

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(self.bucket_name)
    blob = bucket.blob(self.cs_filename, chunk_size=self.CHUNK_SIZE)
    print("     Uploading file {}".format(self.cs_filename));
    blob.upload_from_filename(self.tmppath)

