import requests
import datetime


def now():
    now = datetime.datetime.now()

    return now


def getData(url):
    req = requests.get(url, timeout=3000)
    response = req.json()

    return response


def urlGeneretor(var, date):
    if var is 1:
        # Brasil.io --- Dados Brasil
        url = ('https://brasil.io/api/dataset/covid19/caso/data/?date<{}'
               .format(date))
    elif var is 2:
        # Brasil.io --- Dados Cartórios
        url = ('https://brasil.io/api/dataset/covid19/obito_cartorio/data/?date<{}'
               .format(date))
    elif var is 3:
        # Brasil.api
        pass
    elif var is 4:
        # Brasil.api
        pass
    else:
        # ERROR
        pass

    return url