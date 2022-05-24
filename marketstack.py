'''
########################################################################################################################
Make sure to update the API_KEY variable with your own API key. You can get an API key by logging into your account at https://www.marketstack.com/ or making an account at https://www.marketstack.com/signup.

########################################################################################################################
'''

marketstack_api_key = "YOUR_API_KEY"

def set_api_key(api_key):
    global marketstack_api_key
    marketstack_api_key = api_key

'''
########################################################################################################################
Don't touch anything beneath this line. All you need to do is add your API Key.
########################################################################################################################
'''

import requests
import pandas as pd
from dateutil.parser import parse
import re

marketstack_url = 'http://api.marketstack.com/v1/'

#Error Response Messages for API
limit_error_response = "Limit must be between 1 and 1000."
offset_error_response = "Offset must be between 0 and 1000."
sort_error_response = "Sort must be either 'asc' or 'desc'"

def check_endpoint(endpoint, endpoint_arr):
    if endpoint in endpoint_arr:
        return endpoint
    else:
        raise ValueError("Endpoint: ", endpoint ," not supported.")
    
def check_date_format(date):
    try:
        parse(date)
    except ValueError:
        raise ValueError("Date format not supported. Please format date YYYY-MM-DD or in ISO-8601 format.")
    return date

def check_for_date_format(date):
    date_expression = re.compile('\d{4}-\d{2}-\d{2}')
    if date_expression.match(date) is not None:
        return True
    else:
        return False

def check_feature_support(feature, feature_arr):
    #checks format of feature string to check if it is similar to a date. If so, it will be parsed to check if it is a valid date.
    date_expression = re.compile('\d{4}-\d{2}-\d{2}')
    if date_expression.match(feature) is not None:
        check_date_format(feature)
        return feature
    #if the feature is not in a date format, it then checks if it is in the feature_arr.
    elif feature in feature_arr:
        return feature
    #if it is neither a date format or in the feature_arr, it will raise an error.
    else:
        raise ValueError("Endpoint Feature: ", feature ," not supported.")
            

class MarketStack:
    marketstack_endpoints = ["eod", "intraday", "splits", "dividends", "tickers", "exchanges", "currencies", "timezones"]
    def __init__(self, endpoint):
        #Define marketstack API webhook URL
        self.url = marketstack_url
        #Define marketstack API endpoint and add to URL
        self.endpoint = check_endpoint(endpoint, self.marketstack_endpoints)
        self.url += self.endpoint
        #define parameters for API call. Making sure the API Key is always included.
        self.params = {
            'access_key': marketstack_api_key
        }

    def get_api_response_code(self):
        response = requests.get(self.url, self.params)
        return response

    def get_api_response(self):
        print(self.url, self.params)
        api_result = self.get_api_response_code()
        return api_result.json()

    def get_data(self):
        api_response = self.get_api_response()
        return api_response['data']
    
    def get_data_df(self):
        data = self.get_data()
        df = pd.DataFrame(data)
        return df


class EndOfDay(MarketStack):
    eod_features = ['latest', 'YYYY-MM-DD']
    request_params = {
        "symbols": "", 
        "exchange": "", 
        "sort": ["asc", "desc"], 
        "date_from": "YYYY-MM-DD",
        "date_to": "YYYY-MM-DD", 
        "limit": [1, 1000], 
        "offset": [0, 1000],
    }
    def __init__(self, symbols, exchange = None, sort = None, date_from = None, date_to = None, limit = None, offset = None, feature = None):
        #Define marketstack endpoint as EOD for end of day data
        super().__init__('eod')
        #Define Required parameters for API call
        self.params['symbols'] = symbols
        #Define Optional parameters for API call
        if exchange is not None:
            self.params['exchange'] = exchange
        if sort is not None:
            assert sort in self.request_params['sort'], sort_error_response
            self.params['sort'] = sort
        if date_from is not None:
            self.params['date_from'] = check_date_format(date_from)
        if date_to is not None:
            self.params['date_to'] = check_date_format(date_to)
        if limit is not None:
            assert (limit >= 1 and limit <= 1000), limit_error_response
            self.params['limit'] = limit
        if offset is not None:
            assert (offset >= 0 and offset <= 1000), offset_error_response
            self.params['offset'] = offset
        if feature is not None:
            self.url += '/' + check_feature_support(feature, self.eod_features)
        
class Intraday(MarketStack):
    intraday_features = ['latest', 'YYYY-MM-DD']
    request_params = {
        "symbols": "", 
        "exchange": "", 
        "sort": ["asc", "desc"], 
        "date_from": "YYYY-MM-DD",
        "date_to": "YYYY-MM-DD", 
        "limit": [1, 1000], 
        "offset": [0, 1000],
    }
    def __init__(self, symbols, exchange = None, sort = None, date_from = None, date_to = None, limit = None, offset = None, feature = None):
        #Define marketstack endpoint as EOD for end of day data
        super().__init__('intraday')
        #Define Required parameters for API call
        self.params['symbols'] = symbols
        #Define Optional parameters for API call
        if exchange is not None:
            self.params['exchange'] = exchange
        if sort is not None:
            assert sort in self.request_params['sort'], sort_error_response
            self.params['sort'] = sort
        if date_from is not None:
            self.params['date_from'] = check_date_format(date_from)
        if date_to is not None:
            self.params['date_to'] = check_date_format(date_to)
        if limit is not None:
            assert (limit >= 1 and limit <= 1000), limit
            self.params['limit'] = limit
        if offset is not None:
            assert (offset >= 0 and offset <= 1000), offset_error_response
            self.params['offset'] = offset
        if feature is not None:
            self.url += '/' + check_feature_support(feature, self.intraday_features)

class Splits(MarketStack):
    request_params = {
        "symbols": "",
        "sort": ["asc", "desc"], 
        "date_from": "YYYY-MM-DD",
        "date_to": "YYYY-MM-DD", 
        "limit": [1, 1000], 
        "offset": [0, 1000],
    }
    def __init__(self, symbols, sort = None, date_from = None, date_to = None, limit = None, offset = None):
        #Define marketstack endpoint as EOD for end of day data
        super().__init__('splits')
        #Define Required parameters for API call
        self.params['symbols'] = symbols
        #Define Optional parameters for API call
        if sort is not None:
            assert sort in self.request_params['sort'], sort_error_response
            self.params['sort'] = sort
        if date_from is not None:
            self.params['date_from'] = check_date_format(date_from)
        if date_to is not None:
            self.params['date_to'] = check_date_format(date_to)
        if limit is not None:
            assert (limit >= 1 and limit <= 1000), limit
            self.params['limit'] = limit
        if offset is not None:
            assert (offset >= 0 and offset <= 1000), offset_error_response
            self.params['offset'] = offset

class Dividends(MarketStack):
    request_params = {
        "symbols": "",
        "sort": ["asc", "desc"], 
        "date_from": "YYYY-MM-DD",
        "date_to": "YYYY-MM-DD", 
        "limit": [1, 1000], 
        "offset": [0, 1000],
    }
    def __init__(self, symbols, sort = None, date_from = None, date_to = None, limit = None, offset = None):
        #Define marketstack endpoint as EOD for end of day data
        super().__init__('dividends')
        #Define Required parameters for API call
        self.params['symbols'] = symbols
        #Define Optional parameters for API call
        if sort is not None:
            assert sort in self.request_params['sort'], sort_error_response
            self.params['sort'] = sort
        if date_from is not None:
            self.params['date_from'] = check_date_format(date_from)
        if date_to is not None:
            self.params['date_to'] = check_date_format(date_to)
        if limit is not None:
            assert (limit >= 1 and limit <= 1000), limit
            self.params['limit'] = limit
        if offset is not None:
            assert (offset >= 0 and offset <= 1000), offset_error_response
            self.params['offset'] = offset

class Tickers(MarketStack):
    request_params = {
        "exchange": "",
        "search": "",
        "limit": [1, 1000], 
        "offset": [0, 1000],
    }
    def __init__(self, exchange = None, search = None, limit = None, offset = None, symbol = None, eod = False, splits = False, dividends = False, intraday = False, eod_date = None, eod_latest = False, intraday_latest = False):
        #Define marketstack endpoint as EOD for end of day data
        super().__init__('tickers')
        #Define Optional parameters for API call
        if exchange is not None:
            self.params['exchange'] = exchange
        if search is not None:
            self.params['search'] = search
        if limit is not None:
            assert (limit >= 1 and limit <= 1000), limit
            self.params['limit'] = limit
        if offset is not None:
            assert (offset >= 0 and offset <= 1000), offset_error_response
            self.params['offset'] = offset
        #Define Ticker Features to add to url
        if symbol is not None:
            self.url += '/' + symbol
        if eod is True:
            assert symbol is not None, "Symbol must be specified if eod is True"
            self.url += '/eod'
        if splits is True:
            assert symbol is not None, "Symbol must be specified if splits is True"
            self.url += '/splits'
        if dividends is True:
            assert symbol is not None, "Symbol must be specified if dividends is True"
            self.url += '/dividends'
        if intraday is True:
            assert symbol is not None, "Symbol must be specified if intraday is True"
            self.url += '/intraday'
        if eod_date is not None:
            assert symbol is not None, "Symbol must be specified if eod_date is specified"
            self.url += '/eod/' + check_date_format(eod_date)
        if eod_latest is True:
            assert symbol is not None, "Symbol must be specified if eod_latest is True"
            self.url += '/eod_latest'
        if intraday_latest is True:
            assert symbol is not None, "Symbol must be specified if intraday_latest is True"
            self.url += '/intraday_latest'

class Exchanges(MarketStack):
    request_params = {
        "search": "",
        "limit": [1, 1000], 
        "offset": [0, 1000],
    }
    def __init__(self, search = None, limit = None, offset = None, exchange = None, tickers = False, eod = False, intraday = False, eod_date = None, intraday_date = None, eod_latest = False, intraday_latest = False):
        #Define marketstack endpoint as EOD for end of day data
        super().__init__('exchanges')
        #Define Optional parameters for API call
        if search is not None:
            self.params['search'] = search
        if limit is not None:
            assert (limit >= 1 and limit <= 1000), limit
            self.params['limit'] = limit
        if offset is not None:
            assert (offset >= 0 and offset <= 1000), offset_error_response
            self.params['offset'] = offset
        #Define Ticker Features to add to url
        if exchange is not None:
            self.url += '/' + exchange
        if tickers is True:
            assert exchange is not None, "Exchange must be specified if tickers is True"
            self.url += '/tickers'
        if eod is True:
            assert exchange is not None, "Exchange must be specified if eod is True"
            self.url += '/eod'
        if intraday is True:
            assert exchange is not None, "Exchange must be specified if intraday is True"
            self.url += '/intraday'
        if eod_date is not None:
            assert exchange is not None, "Exchange must be specified if eod_date is specified"
            self.url += '/eod/' + check_date_format(eod_date)
        if intraday_date is not None:
            assert exchange is not None, "Exchange must be specified if intraday_date is specified"
            self.url += '/intraday/' + check_date_format(intraday_date)
        if eod_latest is True:
            assert exchange is not None, "Exchange must be specified if eod_latest is True"
            self.url += '/eod_latest'
        if intraday_latest is True:
            assert exchange is not None, "Exchange must be specified if intraday_latest is True"
            self.url += '/intraday_latest'

class Currencies(MarketStack):
    request_params = {
        "limit": [1, 1000], 
        "offset": [0, 1000],
    }
    def __init__(self, limit = None, offset = None):
        super().__init__('currencies')
        #Define Optional parameters for API call
        if limit is not None:
            assert (limit >= 1 and limit <= 1000), limit
            self.params['limit'] = limit
        if offset is not None:
            assert (offset >= 0 and offset <= 1000), offset_error_response
            self.params['offset'] = offset

class TimeZones(MarketStack):
    request_params = {
        "limit": [1, 1000], 
        "offset": [0, 1000],
    }
    def __init__(self, limit = None, offset = None):
        super().__init__('timezones')
        #Define Optional parameters for API call
        if limit is not None:
            assert (limit >= 1 and limit <= 1000), limit
            self.params['limit'] = limit
        if offset is not None:
            assert (offset >= 0 and offset <= 1000), offset_error_response
            self.params['offset'] = offset

