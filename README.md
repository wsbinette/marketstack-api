# Market Stack API - Python
Thus is a Python API for the [Market Stack](https://marketstack.com/documentation) API. This package will allow you to simply import the python package to use the api rather than having to write the requests yourself.

## Requirements
For this package you'll need to make sure you have the folling requirements installed:
- Requests
    - For running the API requests to the Market Stack API
- Pandas
    - For dataframe handling
- Regex
    - For parsing the dates in requests to for some error handling
- Python-dateutil
    - For parsing the dates in requests to for some error handling

## Installation
To use this package simply clone the git repo into your directory and install the requirements.

```bash
git clone https://github.com/wsbinette/marketstack-api.git
```
### Requirements Installation
For you're convenience, I've included a configuration file, requirements.txt, that will install all the requirements for you. Simply run the following command to install the requirements:
```bash
pip install -r requirements.txt
```
### API Key
After you've made cloned the repo and installed the requirements, you need to get your own Personal API key for the Market Stack API. You can do this by going to the [Market Stack API](https://marketstack.com/documentation) and creating an account. Once you have your key, you can set your key using the "set_api_key" method.

To set your api_key using the built in method, use the code below.

```python
marketstack.set_api_key('YOUR_API_KEY')
```

## How to Use the API
Once you've installed the requirements, cloned the git repo, and gotten your own API key, you can simply import the package at the top of your python project and use it like you would any other package.
```python
import marketstack
```
You can refer to the full docuemntation for the API here: [Market Stack API](https://marketstack.com/documentation). 
Below I'll outline some of the basic usage of the API. 

### API Features
Check the Market Stack API [documentation](https://marketstack.com/documentation) for a full list of features. All the parameters listed there will be present in the API. You can call them like so:

#### Methods
Use these methods in conjunction with the marketstack documentation. Methods will return an object, but you need to specify the data type you want with the sub methods below:

#### Getters

For the API response code: 
```python
marketstack.METHOD.get_api_response_code()
```
For the raw API JSON response: 
```python
use marketstack.METHOD.get_api_response()
```
For the API response data: 
```python
marketstack.METHOD.get_data()

# You can also format the data in a pandas dataframe if you like:
marketstack.METHOD.get_data_df()
```
#### Listed Methods on the Market Stack API
For the API methods that are listed on the marketstack documentation, you can call them like so:

```python
import marketstack

marketstack.set_api_key('YOUR_API_KEY')

#For end of day data
marketstack.EndOfDay(symbols = ["string"], exchange = "string", sort = "string", date_from = "YYYY-MM-DD", date_to= "YYYY-MM-DD", limit= int, offset = int, feature= "string")

#For intraday data
marketstack.Intraday(symbols = ["string"], exchange = "string", sort = "string", date_from = "YYYY-MM-DD", date_to= "YYYY-MM-DD", limit = int, offset = int, feature = "string")

#Splits 
marketstack.Splits(symbols = ["string"], sort = "string", date_from = "YYYY-MM-DD", date_to= "YYYY-MM-DD", limit = int, offset = int)

#For Dividends
marketstack.Dividends(symbols = ["string"], sort = "string", date_from = "YYYY-MM-DD", date_to = "YYYY-MM-DD", limit = int, offset = int)

#Tickers
marketstack.Tickers(exchange = "string", search = "string", limit = int, offset = int, symbol = "string", eod = bool, splits = bool, dividends = bool, intraday = bool, eod_date = "YYYY-MM-DD", eod_latest = bool, intraday_latest = bool)

#Exchanges
marketstack.Exchanges(search = "string", limit = int, offset = int, exhange = "string", tickers =["string"], eod = bool, intraday = bool, eod_date = "YYYY-MM-DD", intraday_date = "YYYY-MM-DD", eod_latest = bool, intraday_latest = bool)

#Currencies
marketstack.Currencies(limit = int, offset = int)

#Time Zones
marketstack.TimeZones(limit = int, offset = int)

```

### Example Usage:
```python
import marketstack

#First set your API key
marketstack.set_api_key('YOUR_API_KEY')

#Once your api key is set you can make calls.

apple_eod = marketstack.EndOfDay('AAPL', sort = 'asc').get_data_df()

```

The above call returns a pandas dataframe with the end of day data for Apple.

```bash
       open      high       low   close      volume adj_high adj_low  adj_close adj_open adj_volume  split_factor  dividend symbol exchange                      date
0   126.010  127.9350  125.9400  127.10  61144792.0     None    None     127.10     None       None           1.0       0.0   AAPL     XNAS  2021-05-24T00:00:00+0000
1   127.820  128.3168  126.3200  126.90  70119179.0     None    None     126.90     None       None           1.0       0.0   AAPL     XNAS  2021-05-25T00:00:00+0000
2   126.955  127.3900  126.4200  126.85  53175620.0     None    None     126.85     None       None           1.0       0.0   AAPL     XNAS  2021-05-26T00:00:00+0000
3   126.440  127.6400  125.2800  125.28  86473226.0     None    None     125.28     None       None           1.0       0.0   AAPL     XNAS  2021-05-27T00:00:00+0000
4   125.570  125.8000  124.5500  124.61  71232700.0     None    None     124.61     None       None           1.0       0.0   AAPL     XNAS  2021-05-28T00:00:00+0000
..      ...       ...       ...     ...         ...      ...     ...        ...      ...        ...           ...       ...    ...      ...                       ...
95  143.060  144.2150  142.7300  143.29  61732656.0     None    None     143.29     None       None           1.0       0.0   AAPL     XNAS  2021-10-07T00:00:00+0000
96  144.030  144.1800  142.5600  142.90  58718700.0     None    None     142.90     None       None           1.0       0.0   AAPL     XNAS  2021-10-08T00:00:00+0000
97  142.270  144.8100  141.8100  142.81  63012662.0     None    None     142.81     None       None           1.0       0.0   AAPL     XNAS  2021-10-11T00:00:00+0000
98  143.230  143.2500  141.0401  141.51  73035862.0     None    None     141.51     None       None           1.0       0.0   AAPL     XNAS  2021-10-12T00:00:00+0000
99  141.235  141.4000  139.2000  140.91  74732031.0     None    None     140.91     None       None           1.0       0.0   AAPL     XNAS  2021-10-13T00:00:00+0000

[100 rows x 15 columns]
```

## Notes
I used the Anaconda environment for development of this package, but you can use any other environment you'd like. If you want more information about Anaconda it's great for data analysis. You can check out their docs and installation instructions here: [Anaconda](https://www.anaconda.com)