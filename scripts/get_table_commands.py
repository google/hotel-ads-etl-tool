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

import argparse
import re

from hotel_ads_beam_utils import HotelAdsApiReports


def run(argv=None):
  """Main executor.

  Args:
    argv: command line arguments.
  """
  parser = argparse.ArgumentParser()
  parser.add_argument('--project', dest='project', help='GCP project id')
  parser.add_argument(
      '--dataset',
      dest='dataset',
      default='hotel_ads_data_transfer',
      help='BigQuery dataset to use for output')
  parser.add_argument(
      '--delete-all-tables',
      dest='delete_all_tables',
      action='store_true',
      help='Includes table deletion commands before the creation ones.')
  parser.add_argument(
      '--delete-dataset',
      dest='delete_dataset',
      action='store_true',
      help='Includes a dataset deletion commands before everything else.')
  parser.add_argument(
      '--account_id',
      dest='account_id',
      help='Hotel Ads Account ID.')
  known_args, _ = parser.parse_known_args(argv)

  hotel_ads_api_reports = HotelAdsApiReports()
  project = known_args.project
  dataset = known_args.dataset + "_" + known_args.account_id
  if known_args.delete_dataset:
    print('echo "Deleting the [{0}] dataset..."'.format(dataset))
    print('bq rm -r {0}'.format(dataset))

  print('echo "Creating the [{0}] dataset..."'.format(dataset))
  print('bq mk {0}'.format(dataset))

  newline_regex = re.compile(r'\n +', re.IGNORECASE)
  for report_name, report_info in hotel_ads_api_reports.REPORTS_INFO.items():
    if known_args.delete_all_tables and not known_args.delete_dataset:
      print('echo "Deleting the [{0}.{1}] table..."'.format(
          dataset, report_name))
      print('bq rm -f {0}.{1}'.format(dataset, report_name))

    print('echo "Creating the [{0}.{1}] table..."'.format(dataset, report_name))
    command = 'bq mk --table --time_partitioning_type=DAY'
    command += ' --time_partitioning_field report_date_id'
    command += ' --description \'{0}\''.format(
        newline_regex.sub(' ', report_info['description']).replace('\'', ''))
    command += ' {0}:{1}.{2}'.format(project, dataset, report_name)
    command += ' {0}'.format(hotel_ads_api_reports.get_flat_schema(report_name))
    print(command)


if __name__ == '__main__':
  run()
