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
pip install facebook_business

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.api import FacebookAdsApi

access_token = 'EAAJWt1T9wRwBAFA0dZAGDYi3584pzIYbH4DKS7FkKGRb5TJk2LfnekjFQjeQkoM1VsFyfi1sQZBwbCGcUOisnhs5UoelW1oRfdZAhvc8YsBi8zOVJ01a0ZCQ9agXDWkDKAlRQ9TdgC4eo48tCPrRmOvZADOsPS1e6XLDkH8QNNyvu0ZCB2MvmKodHlXZA32A7oZD'
ad_account_id = 'act_209987050311319'
app_secret = '5f320ad556bed9fabf191c54ff9a1c9c'
app_id = '658295358341404'
FacebookAdsApi.init(access_token=access_token)

fields = [
    'reach',
    'frequency',
    'impressions',
    'spend',
    'quality_score_organic',
    'quality_score_ectr',
    'quality_score_ecvr',
    'cpp',
    'cpm',
    'clicks',
    'cpc',
]
params = {
    'level': 'account',
    'filtering': [],
    'breakdowns': ['gender'],
    'time_range': {'since':'2020-02-01','until':'2020-05-01'},
}
AdAccount(ad_account_id).get_insights(
    fields=fields,
    params=params,
)
