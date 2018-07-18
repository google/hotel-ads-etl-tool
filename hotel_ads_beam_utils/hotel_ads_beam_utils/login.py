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

import json
import os
import httplib2

from oauth2client.service_account import ServiceAccountCredentials


class HotelAdsApiLogin(object):
  """Utilitarian class to hold connection details to the API."""

  def __init__(self, service_account, key, partner):
    self.key_file = key
    self.account = service_account
    self.partner = partner

  def initialize_credentials(self, scope):
    """Get credentials for use in API requests.

    Generates service account credentials if the key file is present,
    and regular user credentials if the file is not found.
    """

    if os.path.exists(self.key_file):
      creds = ServiceAccountCredentials.from_json_keyfile_name(
          self.key_file, scopes=scope)
      self.credentials = creds

  def authorize(self):
    """Construct a HTTP client that uses the supplied credentials."""

    return credentials.authorize(httplib2.Http())

  def print_creds(self):
    """Prints the Authorization header to use in HTTP requests."""

    cred_dict = json.loads(self.credentials.to_json())

    if 'access_token' in cred_dict:
      print('Authorization: Bearer %s' % (cred_dict['access_token'],))
    else:
      print('creds: %s' % (cred_dict,))

  def get_creds(self):
    """Returns the Authorization header string to use in HTTP requests."""

    cred_dict = json.loads(self.credentials.to_json())

    if 'access_token' in cred_dict:
      return '{}'.format(cred_dict['access_token'])
    else:
      return '{}'.format(cred_dict)

  def get_connection(self):
    """Authenticates and returns an authenticated connection object."""
    http = httplib2.Http()
    self.credentials.refresh(http)
    http = self.credentials.authorize(http)
    return http

  def get_connection_token(self):
    """Authenticastes and returns the Authorization token."""
    http = httplib2.Http()
    self.credentials.refresh(http)
    http = self.credentials.authorize(http)
    return self.get_creds()
