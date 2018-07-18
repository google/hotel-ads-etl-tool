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

import apache_beam as beam
from apache_beam.options.pipeline_options import GoogleCloudOptions
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import StandardOptions
from apache_beam.options.pipeline_options import SetupOptions

from apache_beam.io import ReadFromText

from hotel_ads_beam_utils import HotelAdsApiConnector
from hotel_ads_beam_utils import HotelAdsApiReports
from hotel_ads_beam_utils import SplitInputsDoFn
from hotel_ads_beam_utils import to_table_row


def run(argv=None):

  """Main executor.

  Args:
    argv: command line arguments.
  """

  # Define dataflow options
  api_reports = HotelAdsApiReports()

  pipeline_options = PipelineOptions()
  dt_options = pipeline_options.view_as(DataTransferOptions)
  pipeline_options.view_as(StandardOptions).runner = 'DataflowRunner'
  pipeline_options.view_as(
      GoogleCloudOptions).temp_location = 'gs://{0}/temp'.format(
          dt_options.bucket)
  pipeline_options.view_as(
      GoogleCloudOptions).staging_location = 'gs://{0}/staging'.format(
          dt_options.bucket)

  p = beam.Pipeline(options=pipeline_options)

  dt_options = pipeline_options.view_as(DataTransferOptions)

  print (dt_options)
  api_data = p | 'GetApiData' >> ReadFromText(dt_options.cs_filename)
  report_data = api_data | 'SplitInputs' >> beam.ParDo(
      SplitInputsDoFn()).with_outputs(*list(api_reports.REPORTS_INFO.keys()))

  for report_name, report_info in api_reports.REPORTS_INFO.items():
    particular_report_data = report_data[report_name]

    _ = (
        particular_report_data
        | 'ToTableRows_{0}'.format(report_name) >> beam.Map(
            to_table_row, report_info['schema'])
        | 'WriteToBQ_{0}'.format(report_name) >> beam.io.Write(
            beam.io.BigQuerySink(
                '{0}_{1}.{2}'.format(dt_options.dataset, dt_options.account_id, report_name),
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND)))

  p.run().wait_until_finish()


class DataTransferOptions(PipelineOptions):

  @classmethod
  def _add_argparse_args(cls, parser):
    parser.add_argument(
        '--bucket', dest='bucket', required=True, help='GCP storage bucket')
    parser.add_argument(
        '--dataset',
        dest='dataset',
        default='hotel_ads_dataset',
        help=
        'BigQuery dataset to use for output (default: hotel_ads_data_transfer)')
    parser.add_value_provider_argument(
        '--cs_filename',
        help='Cloud Storage temporary data file')
    parser.add_argument(
        '--account_id',
        dest='account_id',
        help='Hotel Ads Account ID')


if __name__ == '__main__':
  run()
