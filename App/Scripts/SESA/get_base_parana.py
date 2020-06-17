from datetime import datetime
from Scripts.functions import now, urlGenerator, getApi, getPreviousDate, formatDate
from DataBase import tableClass
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

def cleaner(temp_data):
    
    if len(temp_data.columns) > 5:
        over_columns = [temp_data.columns[5:len(temp_data.columns)]]
        temp_data.drop(over_columns[0], inplace=True, axis=1)
    
    columns = [temp_data.columns[1:len(temp_data.columns)]]
    if 'IBGE' in str(columns):
        temp_data = temp_data.drop(['IBGE'], axis=1)      
    
    temp_data = temp_data.dropna(how='all')
    
    arr = temp_data[1:].values

    head = [
        "REGIONAL",
        "MUNICIPIO",
        "CONFIRMADOS",
        "OBITOS"
    ]

    dataset = pd.DataFrame(data=arr,
                          columns=head)

    dataset.dropna(subset=['REGIONAL'], inplace=True)

    return dataset

def catcher():
    
    dataset = pd.DataFrame()
    
    date = datetime.now().date()

    r = requests.get('http://www.saude.pr.gov.br/sites/default/arquivos_restritos/files/documento/2020-0{}/informe_epidemiologico_{}.csv'.format(date.month, formatDate(4, date)))
    r.raise_for_status

    while not r.ok:
        date = getPreviousDate(date)
        r = requests.get('http://www.saude.pr.gov.br/sites/default/arquivos_restritos/files/documento/2020-0{}/informe_epidemiologico_{}.csv'.format(date.month, formatDate(4, date)))
        r.raise_for_status
    
    else: 
        url = ("http://www.saude.pr.gov.br/sites/default/arquivos_restritos/files/documento/2020-0{}/informe_epidemiologico_{}.csv").format(date.month, formatDate(4, date))
        temp_dataset = pd.read_csv(url, sep=';|\t', header=1, engine='python', error_bad_lines=False)
        
        temp_dataset = cleaner(temp_dataset)
        temp_dataset['DATA'] = date

    dataset = pd.concat([dataset, temp_dataset])
    
    dataset.reset_index(drop=True, inplace=True)

    dataset.insert(len(dataset.columns), "insert_date", now())
    
    return dataset

def insertData(session):

    print("Coletando e inserindo dados para SESA-base-Paraná...")

    dataset = catcher()
    
    dbFormat = tableClass.SESA_parana()

    dataset.to_sql('SESA_base_PR', con=session.get_bind(), index_label='id', if_exists='replace', method='multi', chunksize=50000, dtype=dbFormat)

    return ''



