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

IFS=$'|'
arr=($account_ids)
unset IFS
for account_id in ${arr[@]}
do
python create_template.py \
    --project ${project} \
    --bucket ${bucket} \
    --dataset ${dataset}  \
    --account_id ${account_id} \
    --cs-filename ${cs_filename} \
    --requirements_file ${requirements_file} \
    --extra_package ${extra_package} \
    --temp_location gs://${bucket}/temp \
    --staging_location gs://${bucket}/staging \
    --template_location gs://${bucket}/templates/${template}_${account_id}

gsutil cp template_metadata gs://${bucket}/templates/${template}_${account_id}_metadata
done
