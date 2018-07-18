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


class HotelAdsApiReports(object):
  """Utilitarian class to hold schema details of the API."""

  REPORTS_INFO = {
      'audience': {
          'description':
              """Shows performance of bid multipliers on AdWords audience
              lists.""",
          'schema': [
              {
                  'name': 'report_date_id',
                  'type': 'DATE'
              },
              {
                  'name': 'subaccount_id',
                  'type': 'INTEGER'
              },
              {
                  'name': 'audience_list_id',
                  'type': 'STRING'
              },
              {
                  'name': 'device_type',
                  'type': 'STRING'
              },
              {
                  'name': 'date_type',
                  'type': 'STRING'
              },
              {
                  'name': 'price_bucket',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'avg_ad_position',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'impressions',
                  'type': 'INTEGER'
              },
              {
                  'name': 'eligible_impressions',
                  'type': 'INTEGER'
              },
              {
                  'name': 'clicks',
                  'type': 'INTEGER'
              },
              {
                  'name': 'billing_cost_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'conversions',
                  'type': 'INTEGER'
              },
              {
                  'name': 'booked_base_price_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'booked_total_price_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'booked_length_of_stay',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'booking_window_days',
                  'type': 'FLOAT64'
              },
          ]
      },
      'bid_simulation_cpc_fixed': {
          'description':
              """Gives you a quick view of the overall CPC fixed bidding
              landscape and helps you determine what bids to make.""",
          'schema': [
              {
                  'name': 'report_date_id',
                  'type': 'DATE'
              },
              {
                  'name': 'property_id',
                  'type': 'STRING'
              },
              {
                  'name': 'bid_multipliers',
                  'type': 'BOOLEAN'
              },
              {
                  'name': 'uniform',
                  'type': 'BOOLEAN'
              },
              {
                  'name': 'simulated_bid_cpc_fixed_EUR',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'eligible_impr',
                  'type': 'INTEGER'
              },
              {
                  'name': 'actual_impr',
                  'type': 'INTEGER'
              },
              {
                  'name': 'actual_impr_share',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'ad_position_1_impr',
                  'type': 'INTEGER'
              },
              {
                  'name': 'ad_position_1_impr_share',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'clicks',
                  'type': 'INTEGER'
              },
              {
                  'name': 'click_cost_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'conversions',
                  'type': 'INTEGER'
              },
              {
                  'name': 'converted_total_price_usd',
                  'type': 'FLOAT64'
              },
          ]
      },
      'bid_simulation_cpc_percentage': {
          'description':
              """Gives you a quick view of the overall CPC percentage bidding
              landscape and helps you determine what bids to make.""",
          'schema': [
              {
                  'name': 'report_date_id',
                  'type': 'DATE'
              },
              {
                  'name': 'property_id',
                  'type': 'STRING'
              },
              {
                  'name': 'bid_multipliers',
                  'type': 'BOOLEAN'
              },
              {
                  'name': 'uniform',
                  'type': 'BOOLEAN'
              },
              {
                  'name': 'simulated_bid_cpc_percent',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'eligible_impr',
                  'type': 'INTEGER'
              },
              {
                  'name': 'actual_impr',
                  'type': 'INTEGER'
              },
              {
                  'name': 'actual_impr_share',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'ad_position_1_impr',
                  'type': 'INTEGER'
              },
              {
                  'name': 'ad_position_1_impr_share',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'clicks',
                  'type': 'INTEGER'
              },
              {
                  'name': 'click_cost_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'conversions',
                  'type': 'INTEGER'
              },
              {
                  'name': 'converted_total_price_usd',
                  'type': 'FLOAT64'
              },
          ]
      },
      'bid_simulation_target_roas': {
          'description':
              """Gives you a quick view of the overall target ROAS bidding
              landscape and helps you determine what bids to make.""",
          'schema': [
              {
                  'name': 'report_date_id',
                  'type': 'DATE'
              },
              {
                  'name': 'property_id',
                  'type': 'STRING'
              },
              {
                  'name': 'bid_multipliers',
                  'type': 'BOOLEAN'
              },
              {
                  'name': 'uniform',
                  'type': 'BOOLEAN'
              },
              {
                  'name': 'simulated_target_roas',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'eligible_impr',
                  'type': 'INTEGER'
              },
              {
                  'name': 'actual_impr',
                  'type': 'INTEGER'
              },
              {
                  'name': 'actual_impr_share',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'ad_position_1_impr',
                  'type': 'INTEGER'
              },
              {
                  'name': 'ad_position_1_impr_share',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'clicks',
                  'type': 'INTEGER'
              },
              {
                  'name': 'click_cost_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'conversions',
                  'type': 'INTEGER'
              },
              {
                  'name': 'converted_total_price_usd',
                  'type': 'FLOAT64'
              },
          ]
      },
      'bid_simulation_commission_guest_stay': {
          'description':
              """Gives you a quick view of the overall commission guest stay
              bidding landscape and helps you determine what bids to make.""",
          'schema': [
              {
                  'name': 'report_date_id',
                  'type': 'DATE'
              },
              {
                  'name': 'property_id',
                  'type': 'STRING'
              },
              {
                  'name': 'bid_multipliers',
                  'type': 'BOOLEAN'
              },
              {
                  'name': 'uniform',
                  'type': 'BOOLEAN'
              },
              {
                  'name': 'simulated_commission',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'eligible_impr',
                  'type': 'INTEGER'
              },
              {
                  'name': 'actual_impr',
                  'type': 'INTEGER'
              },
              {
                  'name': 'actual_impr_share',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'ad_position_1_impr',
                  'type': 'INTEGER'
              },
              {
                  'name': 'ad_position_1_impr_share',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'clicks',
                  'type': 'INTEGER'
              },
              {
                  'name': 'click_cost_usd',
                  'type': 'INTEGER'
              },
              {
                  'name': 'conversions',
                  'type': 'INTEGER'
              },
              {
                  'name': 'converted_total_price_usd',
                  'type': 'FLOAT64'
              },
          ]
      },
      'book_on_google': {
          'description':
              """Gives you performance data about your direct booking
              flow.""",
          'schema': [
              {
                  'name': 'report_date_id',
                  'type': 'DATE'
              },
              {
                  'name': 'device_type',
                  'type': 'STRING'
              },
              {
                  'name': 'hotel_id',
                  'type': 'STRING'
              },
              {
                  'name': 'hotel_name',
                  'type': 'STRING'
              },
              {
                  'name': 'hotel_group',
                  'type': 'STRING'
              },
              {
                  'name': 'user_country',
                  'type': 'STRING'
              },
              {
                  'name': 'clicks',
                  'type': 'INTEGER'
              },
              {
                  'name': 'avg_cpc_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'cost_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'conv',
                  'type': 'INTEGER'
              },
              {
                  'name': 'conv_rate',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'total_booked_value_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'roas',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'avg_booking_value_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'avg_los',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'avg_daily_rate_usd',
                  'type': 'FLOAT64'
              },
          ]
      },
      'booking': {
          'description':
              """Lists the bookings received through conversion tracking.""",
          'schema': [
              {
                  'name': 'report_date_id',
                  'type': 'DATE'
              },
              {
                  'name': 'hotel_name',
                  'type': 'STRING'
              },
              {
                  'name': 'hotel_id',
                  'type': 'STRING'
              },
              {
                  'name': 'booking_reference',
                  'type': 'STRING'
              },
              {
                  'name': 'booking_date',
                  'type': 'STRING'
              },
              {
                  'name': 'checkin_date',
                  'type': 'STRING'
              },
              {
                  'name': 'length_of_stay',
                  'type': 'INTEGER'
              },
              {
                  'name': 'gross',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'taxes',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'net',
                  'type': 'FLOAT64'
              },
          ]
      },
      'budget': {
          'description':
              """Lists budget performance metrics and estimated missed
              opportunities.""",
          'schema': [
              {
                  'name': 'report_date_id',
                  'type': 'DATE'
              },
              {
                  'name': 'date',
                  'type': 'DATE'
              },
              {
                  'name': 'billing_cost_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'budget_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'spent_pct',
                  'type': 'STRING'
              },
              {
                  'name': 'eligible_impressions',
                  'type': 'INTEGER'
              },
              {
                  'name': 'impressions',
                  'type': 'INTEGER'
              },
              {
                  'name': 'clicks',
                  'type': 'INTEGER'
              },
              {
                  'name': 'elig_impr_over_budget',
                  'type': 'INTEGER'
              },
              {
                  'name': 'est_missed_impr',
                  'type': 'INTEGER'
              },
              {
                  'name': 'est_missed_clicks',
                  'type': 'INTEGER'
              },
              {
                  'name': 'est_unspent_billing_cost_usd',
                  'type': 'FLOAT64'
              },
          ]
      },
      'click_to_call': {
          'description':
              """Shows conversion data and other metrics related to Click to
              Call campaigns.""",
          'schema': [
              {
                  'name': 'report_date_id',
                  'type': 'DATE'
              },
              {
                  'name': 'user_country',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'point_of_sale_name',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'phonenumber',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'clicks',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'cost_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'cpc_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'conversions',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'conv_rate',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'cost_conv_usd',
                  'type': 'FLOAT64'
              },
          ]
      },
      'cross_device_conversions': {
          'description':
              """Shows conversions when a customer clicked on a hotel ad using
              one device and booked the hotel using another device.""",
          'schema': [
              {
                  'name': 'report_date_id',
                  'type': 'DATE'
              },
              {
                  'name': 'display_name',
                  'type': 'STRING'
              },
              {
                  'name': 'campaign_id',
                  'type': 'INTEGER'
              },
              {
                  'name': 'hotel_country',
                  'type': 'STRING'
              },
              {
                  'name': 'user_country',
                  'type': 'STRING'
              },
              {
                  'name': 'device_type',
                  'type': 'STRING'
              },
              {
                  'name': 'conversions',
                  'type': 'INTEGER'
              },
              {
                  'name': 'estimated_cross_device_conversions',
                  'type': 'INTEGER'
              },
              {
                  'name': 'total_conversions',
                  'type': 'INTEGER'
              },
          ]
      },
      'commissions_guest_stay': {
          'description':
              """Provides commissions net of guest stay and other details about
              billing.""",
          'schema': [
              {
                  'name': 'report_date_id',
                  'type': 'DATE'
              },
              {
                  'name': 'start_date',
                  'type': 'STRING'
              },
              {
                  'name': 'end_date',
                  'type': 'STRING'
              },
              {
                  'name': 'reported_stay_nights',
                  'type': 'INTEGER'
              },
              {
                  'name': 'stays_reconciled_lt_30_days',
                  'type': 'STRING'
              },
              {
                  'name': 'stays_reconciled_lt_30_days_pct',
                  'type': 'STRING'
              },
              {
                  'name': 'stays_reconciled_30_60_days',
                  'type': 'STRING'
              },
              {
                  'name': 'stays_reconciled_30_60_days_pct',
                  'type': 'STRING'
              },
              {
                  'name': 'stays_reconciled_60_90_days',
                  'type': 'STRING'
              },
              {
                  'name': 'stays_reconciled_60_90_days_pct',
                  'type': 'STRING'
              },
              {
                  'name': 'stays_reconciled_gt_90_days',
                  'type': 'STRING'
              },
              {
                  'name': 'stays_reconciled_gt_90_days_pct',
                  'type': 'STRING'
              },
              {
                  'name': 'reported_commission_payment_usd',
                  'type': 'STRING'
              },
              {
                  'name': 'payment_reconciled_lt_30_days_usd',
                  'type': 'STRING'
              },
              {
                  'name': 'payment_reconciled_lt_30_days_pct',
                  'type': 'STRING'
              },
              {
                  'name': 'payment_reconciled_30_60_days_usd',
                  'type': 'STRING'
              },
              {
                  'name': 'payment_reconciled_30_60_days_pct',
                  'type': 'STRING'
              },
              {
                  'name': 'payment_reconciled_60_90_days_usd',
                  'type': 'STRING'
              },
              {
                  'name': 'payment_reconciled_60_90_days_pct',
                  'type': 'STRING'
              },
              {
                  'name': 'payment_reconciled_gt_90_days_usd',
                  'type': 'STRING'
              },
              {
                  'name': 'payment_reconciled_gt_90_days_pct',
                  'type': 'STRING'
              },
          ]
      },
      'fenced_rates': {
          'description':
              """Provides details on the traffic received from each offer which
              is based on the end-user's device and domain (if you implement
              fenced rates).""",
          'schema': [
              {
                  'name': 'report_date_id',
                  'type': 'DATE'
              },
              {
                  'name': 'hotel_country',
                  'type': 'STRING'
              },
              {
                  'name': 'hotel_id',
                  'type': 'INTEGER'
              },
              {
                  'name': 'property',
                  'type': 'STRING'
              },
              {
                  'name': 'device_type',
                  'type': 'STRING'
              },
              {
                  'name': 'rate_rule_id',
                  'type': 'STRING'
              },
              {
                  'name': 'user_country',
                  'type': 'STRING'
              },
              {
                  'name': 'ad_position',
                  'type': 'INTEGER'
              },
              {
                  'name': 'price_bucket',
                  'type': 'INTEGER'
              },
              {
                  'name': 'impressions',
                  'type': 'INTEGER'
              },
              {
                  'name': 'eligible_impressions',
                  'type': 'INTEGER'
              },
              {
                  'name': 'clicks',
                  'type': 'INTEGER'
              },
              {
                  'name': 'billing_cost_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'conversions',
                  'type': 'INTEGER'
              },
          ]
      },
      'performance': {
          'description':
              """Includes the performance report, plus additional conversion
              tracking-specific fields. If no report_type value is provided,
              the Reports API returns the dates that are available for this
              report type.""",
          'schema': [
              {
                  'name': 'report_date_id',
                  'type': 'DATE'
              },
              {
                  'name': 'subaccount_id',
                  'type': 'STRING'
              },
              {
                  'name': 'property',
                  'type': 'STRING'
              },
              {
                  'name': 'country',
                  'type': 'STRING'
              },
              {
                  'name': 'device_type',
                  'type': 'STRING'
              },
              {
                  'name': 'hotel_id',
                  'type': 'INTEGER'
              },
              {
                  'name': 'check_in_date',
                  'type': 'STRING'
              },
              {
                  'name': 'date_type',
                  'type': 'STRING'
              },
              {
                  'name': 'length_of_stay',
                  'type': 'INTEGER'
              },
              {
                  'name': 'price_bucket',
                  'type': 'INTEGER'
              },
              {
                  'name': 'slot',
                  'type': 'STRING'
              },
              {
                  'name': 'slot_position',
                  'type': 'INTEGER'
              },
              {
                  'name': 'ad_position',
                  'type': 'INTEGER'
              },
              {
                  'name': 'impressions',
                  'type': 'INTEGER'
              },
              {
                  'name': 'eligible_impressions',
                  'type': 'INTEGER'
              },
              {
                  'name': 'clicks',
                  'type': 'INTEGER'
              },
              {
                  'name': 'billing_cost_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'conversions',
                  'type': 'INTEGER'
              },
              {
                  'name': 'booked_base_price_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'booked_total_price_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'booked_length_of_stay',
                  'type': 'INTEGER'
              },
              {
                  'name': 'booking_window_days',
                  'type': 'INTEGER'
              },
          ],
      },
      'performance_with_click_type': {
          'description':
              """Includes the same information as the performance report, but
              also includes the click type, which is either "standard" (for
              the standard booking module) or "room booking module".""",
          'schema': [
              {
                  'name': 'report_date_id',
                  'type': 'DATE'
              },
              {
                  'name': 'subaccount_id',
                  'type': 'STRING'
              },
              {
                  'name': 'property',
                  'type': 'STRING'
              },
              {
                  'name': 'country',
                  'type': 'STRING'
              },
              {
                  'name': 'device_type',
                  'type': 'STRING'
              },
              {
                  'name': 'hotel_id',
                  'type': 'INTEGER'
              },
              {
                  'name': 'check_in_date',
                  'type': 'STRING'
              },
              {
                  'name': 'date_type',
                  'type': 'STRING'
              },
              {
                  'name': 'click_type',
                  'type': 'STRING'
              },
              {
                  'name': 'length_of_stay',
                  'type': 'INTEGER'
              },
              {
                  'name': 'price_bucket',
                  'type': 'INTEGER'
              },
              {
                  'name': 'slot',
                  'type': 'STRING'
              },
              {
                  'name': 'slot_position',
                  'type': 'INTEGER'
              },
              {
                  'name': 'ad_position',
                  'type': 'INTEGER'
              },
              {
                  'name': 'impressions',
                  'type': 'INTEGER'
              },
              {
                  'name': 'eligible_impressions',
                  'type': 'INTEGER'
              },
              {
                  'name': 'clicks',
                  'type': 'INTEGER'
              },
              {
                  'name': 'billing_cost_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'conversions',
                  'type': 'INTEGER'
              },
              {
                  'name': 'booked_base_price_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'booked_total_price_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'booked_length_of_stay',
                  'type': 'INTEGER'
              },
              {
                  'name': 'booking_window_days',
                  'type': 'INTEGER'
              },
          ]
      },
      'price_accuracy': {
          'description':
              """Lists a sample set of itineraries and the date/times when
              prices for those itineraries were fetched and cached.""",
          'schema': [
              {
                  'name': 'report_date_id',
                  'type': 'DATE'
              },
              {
                  'name': 'partner',
                  'type': 'STRING'
              },
              {
                  'name': 'hotel',
                  'type': 'INTEGER'
              },
              {
                  'name': 'check_in_date',
                  'type': 'STRING'
              },
              {
                  'name': 'length_of_stay',
                  'type': 'INTEGER'
              },
              {
                  'name': 'fetched_price',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'fetched_tax',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'fetched_currency',
                  'type': 'STRING'
              },
              {
                  'name': 'fetched_time',
                  'type': 'STRING'
              },
              {
                  'name': 'cached_price',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'cached_tax',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'cached_currency',
                  'type': 'STRING'
              },
              {
                  'name': 'cached_time',
                  'type': 'STRING'
              },
              {
                  'name': 'corrected_time',
                  'type': 'STRING'
              },
              {
                  'name': 'incorrect_updates',
                  'type': 'STRING'
              },
              {
                  'name': 'url',
                  'type': 'STRING'
              },
              {
                  'name': 'deal',
                  'type': 'STRING'
              },
              {
                  'name': 'validation_key',
                  'type': 'STRING'
              },
              {
                  'name': 'price_history_key',
                  'type': 'STRING'
              },
              {
                  'name': 'rate_rule_id',
                  'type': 'STRING'
              },
              {
                  'name': 'hotel_country',
                  'type': 'STRING'
              },
              {
                  'name': 'subkey',
                  'type': 'STRING'
              },
          ]
      },
      'price_competitiveness': {
          'description':
              """Provides insights into how your prices compare to competitors'
              prices on the same hotel itineraries.""",
          'schema': [
              {
                  'name': 'report_date_id',
                  'type': 'DATE'
              },
              {
                  'name': 'user_country',
                  'type': 'STRING'
              },
              {
                  'name': 'hotel_id',
                  'type': 'INTEGER'
              },
              {
                  'name': 'check_in_date',
                  'type': 'STRING'
              },
              {
                  'name': 'length_of_stay',
                  'type': 'INTEGER'
              },
              {
                  'name': 'slotted_partner_count_bucketed',
                  'type': 'STRING'
              },
              {
                  'name': 'cheapest_slotted_price_partner_type',
                  'type': 'STRING'
              },
              {
                  'name': 'hotel_impressions',
                  'type': 'INTEGER'
              },
              {
                  'name': 'impressions_with_participation',
                  'type': 'INTEGER'
              },
              {
                  'name': 'slotted_impressions',
                  'type': 'INTEGER'
              },
              {
                  'name': 'missed_participation_no_price_lq_technical_issue',
                  'type': 'INTEGER'
              },
              {
                  'name': 'missed_participation_no_price_lq_not_triggerred',
                  'type': 'INTEGER'
              },
              {
                  'name': 'missed_participation_no_price_lq_not_run',
                  'type': 'INTEGER'
              },
              {
                  'name': 'missed_participation_no_price_lq_unavailable',
                  'type': 'INTEGER'
              },
              {
                  'name': 'missed_participation_no_availability',
                  'type': 'INTEGER'
              },
              {
                  'name': 'average_ad_position',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'average_daily_rate_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'average_booked_total_price_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'average_daily_rate_lowest_delta_usd',
                  'type': 'FLOAT64'
              },
              {
                  'name': 'clicks',
                  'type': 'INTEGER'
              },
          ]
      },
      'top_opportunity': {
          'description':
              """Lists opportunities you might have missed per hotel over a
              7-day period. Includes breakdowns of missed opportunities by
              type.""",
          'schema': [
              {
                  'name': 'report_date_id',
                  'type': 'DATE'
              },
              {
                  'name': 'hotel_name',
                  'type': 'STRING'
              },
              {
                  'name': 'hotelid',
                  'type': 'STRING'
              },
              {
                  'name': 'hotel_country',
                  'type': 'STRING'
              },
              {
                  'name': 'hotel_impressions',
                  'type': 'STRING'
              },
              {
                  'name': 'hotel_clicks',
                  'type': 'STRING'
              },
              {
                  'name': 'hotel_ctr',
                  'type': 'STRING'
              },
              {
                  'name': 'hotel_average_lead_value_usd',
                  'type': 'STRING'
              },
              {
                  'name': 'partner_eligible_impressions',
                  'type': 'STRING'
              },
              {
                  'name': 'partner_participation_rate',
                  'type': 'STRING'
              },
              {
                  'name': 'partner_missed_participation',
                  'type': 'STRING'
              },
              {
                  'name': 'partner_impressions',
                  'type': 'STRING'
              },
              {
                  'name': 'partner_impression_share',
                  'type': 'STRING'
              },
              {
                  'name': 'partner_missed_impressions',
                  'type': 'STRING'
              },
              {
                  'name': 'partner_clicks',
                  'type': 'STRING'
              },
              {
                  'name': 'partner_ctr',
                  'type': 'STRING'
              },
              {
                  'name': 'partner_click_share',
                  'type': 'STRING'
              },
              {
                  'name': 'missed_participation_blacklisted_hotels',
                  'type': 'STRING'
              },
              {
                  'name': 'missed_participation_no_availability',
                  'type': 'STRING'
              },
              {
                  'name': 'missed_participation_no_pos',
                  'type': 'STRING'
              },
              {
                  'name': 'missed_participation_live_query_technical_issue',
                  'type': 'STRING'
              },
              {
                  'name': 'missed_participation_live_query_not_triggered',
                  'type': 'STRING'
              },
              {
                  'name': 'missed_participation_live_query_not_run',
                  'type': 'STRING'
              },
              {
                  'name': 'missed_participation_live_query_unavailable',
                  'type': 'STRING'
              },
              {
                  'name': 'missed_participation_no_taxes_breakdown',
                  'type': 'STRING'
              },
              {
                  'name': 'missed_participation_other',
                  'type': 'STRING'
              },
              {
                  'name': 'missed_impressions_no_bid',
                  'type': 'STRING'
              },
              {
                  'name': 'missed_impressions_spending_cap_reached',
                  'type': 'STRING'
              },
              {
                  'name': 'missed_impressions_insufficient_bid',
                  'type': 'STRING'
              },
              {
                  'name': 'missed_impressions_linked_account',
                  'type': 'STRING'
              },
              {
                  'name': 'missed_impressions_other',
                  'type': 'STRING'
              },
          ]
      }
  }

  def get_flat_schema(self, report_name):
    schema = []
    for field in self.REPORTS_INFO[report_name]['schema']:
      schema.append('{0}:{1}'.format(field['name'], field['type']))
    return ','.join(schema)
