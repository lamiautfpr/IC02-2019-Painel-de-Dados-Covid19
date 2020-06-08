from datetime import datetime, timedelta
import requests
import datetime
import pandas as pd
import numpy as np


def now():
    n = datetime.datetime.now()

    return n


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
         # Brasil_API --- Dados Mundo
        url = ('https://covid19-brazil-api.now.sh/api/report/v1/countries')
    elif var == 5:
        # Painel_insumos
        url = ('https://covid-insumos.saude.gov.br/paineis/insumos/lista_csv_painel.php?output=csv')


def getApi(url, format='json'):     #json = formato padrão
    if format == 'json':
        req = requests.get(url, timeout=3000)
        if req.status_code == 200:
            response = req.json()
            return response
        else:
            return False
    elif format == 'csv':
        df = pd.read_csv(url, engine='python', sep=',|;')
        return df


def formatDate(var, date):

    if var == 1:
        # Brasil.io
        pass
    elif var == 2:
        # Brasil.api
        date = date.strftime('%Y%m%d')
    elif var == 3:
        # BD Brasil.api to datetime
        date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")        
    else:
        pass

    return date


def getNextDate(date):

    date += timedelta(days=1)

    return date
