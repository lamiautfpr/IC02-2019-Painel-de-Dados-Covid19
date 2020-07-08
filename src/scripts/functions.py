import requests
import json
from datetime import datetime, timedelta


def now():
    now = datetime.now()
    return now


def format_date(date):
    date = date.strftime('%d_%m_%Y')
    return date


def previous_date(date):
    date -= timedelta(days=1)
    return date


def next_date(date):
    date += timedelta(days=1)
    return date


def url_generator(var, date):
    if var == 1:
        # brapi_nacional
        url = ('https://covid19-brazil-api.now.sh/api/report/v1/brazil/{}'
               .format(date))
    else:
        # brapi_mundial
        url = ('https://covid19-brazil-api.now.sh/api/report/v1/countries')
    return url


def get_api(url):
    content = requests.get(url).json()
    data = content.get('data')
    return data


def format_date(var, date):
    if var == 1:
        # brapi
        date = date.strftime('%Y%m%d')
    elif var == 2:
        # bd brapi to datetime
        date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
    else:
        date = date.strftime('%d_%m_%Y')
    return date
