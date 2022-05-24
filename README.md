# Market Stack API - Python
Thus is a Python API for the [Market Stack](https://marketstack.com/documentation) API. This package will allow you to simply import the python package to use the api rather than having to write the requests yourself.

## Requirements
For this package you'll need to make sure you have the folling requirements installed:
- Requests
    For running the API requests to the Market Stack API
- Pandas
    For dataframe handling
- Regex
    For parsing the dates in requests to for some error handling
- Python-dateutil
    For parsing the dates in requests to for some error handling

## Installation
To use this package simply clone the git repo into your directory and install the requirements.

```bash
git clone https://github.com/wsbinette/marketstack-api.git
```

For you're convenience, I've included a configuration file, requirements.txt, that will install all the requirements for you. Simply run the following command to install the requirements:
```bash
pip install -r requirements.txt
```

After you've made cloned the repo and installed the requirements, you need to get your own Personal API key for the Market Stack API. You can do this by going to the [Market Stack API](https://marketstack.com/documentation) and creating an account. Once you have your key, you can set your key in one of two ways.


## How to Use the API
Once you've installed the requirements, cloned the git repo, and gotten your own API key, you can simply import the package at the top of your python project and use it like you would any other package.
```python
import marketstack
```
You can refer to the full docuemntation for the API here: [Market Stack API](https://marketstack.com/documentation). 
Below I'll outline some of the basic usage of the API. 

### Example Usage:
```python
import marketstack

#First set your API key
marketstack.set_api_key('YOUR_API_KEY')

#Once your api key is set you can make calls.

apple_eod = marketstack.EndOfDay('AAPL)


```

## Notes
I used the Anaconda environment for development of this package, but you can use any other environment you'd like. If you want more information about Anaconda it's great for data analysis. You can check out their docs and installation instructions here: [Anaconda](https://www.anaconda.com)