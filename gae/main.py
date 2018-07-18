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
"""App Engine app to serve as an endpoint for the scheduling of the ETL."""

from __future__ import print_function

from datetime import datetime
from datetime import date
from datetime import timedelta

import flask
from flask import Flask

import sys
import os
# this is necessary for GAE to load the hotel_ads_beam_connector package
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

from hotel_ads_beam_utils import HotelAdsApiConnector
from hotel_ads_beam_utils import HotelAdsApiReports

from googleapiclient.discovery import build
from google.cloud import bigquery
from oauth2client.client import GoogleCredentials

app = Flask(__name__)

BASE_PATH = '.'


def get_data():
  return


@app.route('/230e7f84-5eab-44c0-8ad4-968740444803', methods=['GET'])
def call_handler():

  # Hide the handler for not cron jobs (we are not returning a 403 as we want to
  # purposefully hide this endpoint)

  if 'X-Appengine-Cron' not in flask.request.headers:
    flask.abort(404)

  # TODO: PASTE HERE THE CONTENTS OF THE scripts/config.sh FILE

  # END OF PASTE SECTION

  known_args = {
      'account_ids': account_ids,
      'date_1_ago': (date.today() - timedelta(1)),
      'date_2_ago': (date.today() - timedelta(2)),
      'date_3_ago': (date.today() - timedelta(3)),
      'bucket': bucket,
      'cs_filename': cs_filename,
      'dataset': dataset,
      'project': project,
      'key_file': '{}/keyfile.json'.format(BASE_PATH),
      'partner_names': partner_names,
      'template': template,
      'zone': zone
  }

  # The report_dates_list variable defines the dates to be extracted.
  report_dates_list = [
      known_args['date_1_ago'], known_args['date_2_ago'],
      known_args['date_3_ago']
  ]

  # Loop through each account
  for account_id, partner_name in zip(known_args['account_ids'].split('|'),
                                      known_args['partner_names'].split('|')):
    dataset = '{0}_{1}'.format(known_args['dataset'], account_id)

    # Get the data from the Hotel Ads API
    api_connector = HotelAdsApiConnector(
        account_id=account_id,
        bucket_name=known_args['bucket'],
        key_file=known_args['key_file'],
        partner_name=partner_name)

    counter = 0
    for report_date in report_dates_list:
      api_connector.run('{}.{}.{}'.format(cs_filename, account_id, counter),
                        report_date.strftime('%Y%m%d'))
      counter += 1

    credentials = GoogleCredentials.get_application_default()
    service = build('dataflow', 'v1b3', credentials=credentials)

    # Delete previously loaded data
    api_reports = HotelAdsApiReports()
    bigquery_client = bigquery.Client(project=known_args['project'])
    job_config = bigquery.QueryJobConfig()
    job_config.use_legacy_sql = False
    for report_name in api_reports.REPORTS_INFO.keys():
      for report_date in report_dates_list:
        query = (
            'DELETE FROM `{dataset}.{table}` WHERE report_date_id = "{date}"'
            .format(
                dataset=dataset,
                table=report_name,
                date=report_date.strftime('%Y-%m-%d')))
        _ = bigquery_client.query(query, job_config=job_config)

    # Create the dataflow job
    counter = 0
    for report_date in report_dates_list:
      job_name = '{0}-{1}-{2}'.format(
          dataset.replace('_', '-'), report_date,
          datetime.today().strftime('%Y%m%d%H%M%S'))

      gcs_path = 'gs://{bucket}/templates/{template}_{account_id}'.format(
          bucket=known_args['bucket'],
          template=known_args['template'],
          account_id=account_id)

      body = {
          'jobName': '{jobname}'.format(jobname=job_name),
          'parameters': {
              'cs_filename':
                  'gs://{bucket}/{cs_filename}.{account_id}.{counter}'.format(
                      bucket=known_args['bucket'],
                      cs_filename=known_args['cs_filename'],
                      account_id=account_id,
                      counter=counter)
          },
          'environment': {
              'tempLocation':
                  'gs://{bucket}/temp'.format(bucket=known_args['bucket']),
              'zone':
                  known_args['zone']
          }
      }

      df_request = service.projects().templates().launch(
          projectId=known_args['project'], gcsPath=gcs_path, body=body)
      response = df_request.execute()
      print(response)
      counter += 1
  return 'Ok'


@app.errorhandler(404)
def page_not_found(e):
  return 'Not Found', 404


@app.route('/')
def test_handler():
  return '42'


if __name__ == '__main__':
  # This is used when running locally. Gunicorn is used to run the
  # application on Google App Engine. See entrypoint in app.yaml.
  app.run(host='0.0.0.0', port=8080, debug=True)
