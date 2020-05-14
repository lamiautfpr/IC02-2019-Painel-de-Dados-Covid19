import requests
import datetime


def now():
    n = datetime.datetime.now()

    return n


def getData(url):
    req = requests.get(url, timeout=3000)
    response = req.json()

    return response


def urlGenerator(var, date=now()):
    if var == 1:
        # Brasil.io --- Dados Brasil
        url = ('https://brasil.io/api/dataset/covid19/caso/data/')
    elif var == 2:
        # Brasil.io --- Dados Cartórios
        url = ('https://brasil.io/api/dataset/covid19/obito_cartorio/data/')
    elif var == 3:
        # Brasil_API --- Dados Brasil
        url = ('https://covid19-brazil-api.now.sh/api/report/v1/brazil/{}').format(date)  #todo: formatar p/ string
    elif var == 4:
        # Brasil.api
        pass
    else:
        # ERROR
        pass

    return url