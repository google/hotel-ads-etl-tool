#!/bin/bash
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

source ./config.sh

# Create the bucket
gsutil mb -p "${project}" -c "${storage_class}" -l "${storage_region}" "gs://${bucket}/"

# Compile the package and install it into the dist locations
(cd ../hotel_ads_beam_utils/; \
  mkdir ../gae/dist/; \
  mkdir ../gae/lib/; \
  sudo python setup.py sdist; \
  sudo pip install . --upgrade; \
  pip install -t ../gae/lib/ . --upgrade; \
  cp dist/* ../gae/dist/)

# Create the dataset and tables
IFS=$'|'
arr=($account_ids)
unset IFS
for account_id in ${arr[@]}
do
python ./get_table_commands.py \
    --project "${project}" \
    --dataset "${dataset}" \
    --account_id "${account_id}" | sh
done

# Create the flow
sudo pip install apache_beam[gcp]
IFS=$'|'
arr=($account_ids)
unset IFS
for account_id in ${arr[@]}
do
python ./create_template.py \
    --project "${project}" \
    --bucket "${bucket}" \
    --dataset "${dataset}"  \
    --account_id "${account_id}" \
    --cs-filename "${cs_filename}" \
    --requirements_file "${requirements_file}" \
    --extra_package "${extra_package}" \
    --temp_location "gs://${bucket}/temp" \
    --staging_location "gs://${bucket}/staging" \
    --template_location "gs://${bucket}/templates/${template}"
done

gsutil cp template_metadata "gs://${bucket}/templates/${template}_metadata"

# Deploy the GAE Application
(cd ../gae/; \
  gcloud app create --region=${app_engine_region}; \
  gcloud app deploy --quiet; \
  gcloud app deploy cron.yaml --quiet)

# Enjoy!
