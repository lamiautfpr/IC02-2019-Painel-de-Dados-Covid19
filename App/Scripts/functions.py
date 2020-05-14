import requests
from datetime import datetime, timedelta
import json

def now():
    now = datetime.datetime.now()

    return now


# def formatDate(date):
#     datetimeobject = datetime.strptime(date,"%d-%m-%Y")
#     date = datetimeobject.strftime('%d%m%Y')

#     return date


def urlGeneretor(var, date):
    if var == 1:
        # Brasil.io --- Dados Brasil
        url = ('https://brasil.io/api/dataset/covid19/caso/data/?date<{}'
            .format(date))
    elif var == 2:
        # Brasil.io --- Dados Cartórios
        url = ('https://brasil.io/api/dataset/covid19/obito_cartorio/data/?date<{}'
            .format(date))
    elif var == 3:
        # Brasil.api
        url = ('https://covid19-brazil-api.now.sh/api/report/v1/brazil/{}'
            .format(formatDate(date)))
    elif var == 4:
        url = ('https://covid19-brazil-api.now.sh/api/report/v1/countries')
    else:
        # ERROR
        pass

    return url


def getApi(url):
    res = requests.request("GET", url)
    if res.status_code == 200:
        res = json.loads(res.content)
    else:
        return False

    return res

def formatDate(var, date):
    
    if var == 1:
    #Brasil.io
        pass
    elif var == 2:
    #Brasil.api
        date = date.strftime('%Y%m%d')
    else:
        pass
    
    return date

def getNextDate(date):

    date += timedelta(1)
    
    return date
