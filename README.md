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
To use this package simply clone the git repositor into your directory and install the requirements.

```bash
git clone PACKAGE_URL
```

For you're convenience, I've included a configuration file, requirements.txt, that will install all the requirements for you. Simply run the following command to install the requirements:
```bash
pip install -r requirements.txt
```

I used the Anaconda environment for development of this package, but you can use any other environment you'd like. If you want more information about Anaconda it's great for data analysis. You can check out their docs and installation instructions here: [Anaconda](https://www.anaconda.com)

## How to Use
Once you've installed the requirements and cloned the git repo, you can simply import the package at the top of your python project and use it like you would any other package.
```python
import marketstack
```
