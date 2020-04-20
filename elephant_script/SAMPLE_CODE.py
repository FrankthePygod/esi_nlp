# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.api import FacebookAdsApi

access_token = 'EAAJWt1T9wRwBACVwPa7DpmMrk6ZAFSnfIpwavQJc9cjtHHfRFa48debb5eKWhLYwV2QKjAP0tkoH6hLZBZC0z5ZBnFQa8oLApYzWfwKsfswo4GIZANexohhc82DZBIvDChxzhsZCctVdJRDYM5fZC6N9Ifz0Uz34SnvZABNDbOYu74SJxkgyuGV7p'
ad_account_id = 'act_481286649315818'
app_secret = '5f320ad556bed9fabf191c54ff9a1c9c'
app_id = '658295358341404'
FacebookAdsApi.init(access_token=access_token)

fields = [
    'clicks',
    'cpc',
    'estimated_ad_recallers',
    'estimated_ad_recall_rate',
    'cost_per_estimated_ad_recallers',
    'date_start',
    'date_stop',
    'account_id',
    'account_name',
    'campaign_name',
    'campaign_id',
    'adset_id',
    'adset_name',
    'objective',
    'date_start',
    'date_stop'
]
params = {
    'level': 'ad',
    'filtering': [],
    'breakdowns': [],
    'time_range': {'since':'2020-02-01','until':'2020-05-01'},
}
a = AdAccount(ad_account_id).get_insights(
    fields=fields,
    params=params,
)
type(a)
a

import pandas as pd
df = pd.DataFrame(a)
df

pwd

df.to_csv('C:/Users/xqm50/esi_nlp/elephant_script/test_api.csv',index =False)
