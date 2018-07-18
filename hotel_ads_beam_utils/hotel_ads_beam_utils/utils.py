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

import datetime
import re


def to_table_row(entry, schema):
  """Creates a dict for every record in order to be used by BigQuery Sink."""

  index = 0
  entry_dict = {}

  values = entry[2:]
  for schema_item in schema:
    field_name = schema_item['name']
    field_type = schema_item['type']
    field_value = values[index]

    # Validate input
    if field_type == 'BOOLEAN':
      if re.search('(?i)^(yes|true)$', field_value):
        field_value = True
      elif re.search('(?i)^(no|false)', field_value):
        field_value = False
      else:
        field_value = None
    if field_type != 'STRING' and field_value == '':
      field_value = None
    if field_type == 'DATE':
      if re.search('^[0-9]{8}$', field_value):
        # Converts 20180130 to 2018-01-30
        field_value = datetime.date.strftime(
            datetime.datetime.strptime(field_value, '%Y%m%d'), '%Y-%m-%d')

    # Add to return dict
    entry_dict[field_name] = field_value
    index += 1

  return entry_dict
