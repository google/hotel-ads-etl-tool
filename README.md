# Hotel Ads ETL Tool

This repository contains a tool that provides methods to extract information
from the [Hotel Ads API Reports](https://developers.google.com/hotels/hotel-ads/api-reference/v20/reports-api-v2), transform it using Dataflow/Apache Beam  and insert it into BigQuery tables in Google Cloud Platform.

The tool is composed of the following parts:

- A python package that contains methods to extract data from the Hotel Ads
  API to a file, and Apache Beam custom functions to be used by the pipeline.

- A dataflow job template in charge of transforming the data in the file and
  inserting it into BigQuery.
- A python App Engine script that executes the extraction of the data, saves it
  in cloud storage, and invokes the dataflow template.

Alternatives: If needed, the python App Engine script can be modified to run
locally on a server or another orchestration system, as it doesn't depend on
App Engine to run. Also, the apache beam job can be run (after modifying the
script accordingly) in any managed or unmanaged Apache Beam instance.

This is not an officially supported Google product.

## Prerequisites

1. Access to the Hotel Ads API. Follow the steps of section "Setting up
   OAuth 2.0" in the [API
   Authentication](https://developers.google.com/hotels/hotel-ads/api-reference/api-auth)
   page to get an authorized key.

   Note: in Step 3, select JSON for the Key Type, as this tool uses that format to
   authenticate.

2. A Google Cloud Platform project, to hold the scripts and the data.

3. Enable the Cloud Storage, BigQuery and Dataflow APIs.

## Configuration Steps

The configuration steps will be using the google cloud console, but it can also
be run into a local server/workstation with the google cloud sdk installed.

1. Login to GCP using gcloud

```
gcloud auth login
```

2. Clone the repository into the local filesystem

```
git clone http://giturl.com/...
```

3. Copy the JSON keyfile into the `gae/` directory.

4. Copy the file `scripts/config.sh.sample` to `scripts/config.sh`, and
modify the latter with the appropriated values:

```
  project=''
  account_ids=''
  partner_names=''
  zone=''
  app_engine_region=''
  storage_region=''
  storage_class='Regional'
  bucket='hotel-ads-data-transfer'
  cs_filename='hotel-ads-data-transfer-file'
  dataset='hotel_ads_dataset'
  key_file='keyfile.json'
  template='HotelAdsDataTransfer'
```
   The fields `account_ids` and `partner_names` are "|" separated lists, and must have the same number of elements each.

5. Copy the contents of the file `scripts/config.sh` to the indicated section in
   file `gae/main.py`

```
  # TODO: PASTE HERE THE CONTENTS OF THE scripts/config.sh FILE


  # END OF PASTE SECTION
```

6. Execute the provisioning script `autoprovision.sh`

   Note: If you prefer to control all the tasks performed by the script, you can
   execute the commands inside the script manually.

