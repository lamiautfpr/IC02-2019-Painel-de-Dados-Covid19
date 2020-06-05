from datetime import datetime
from Scripts.functions import now, urlGenerator, getApi, getPreviousDate, formatDate
from DataBase import tableClass
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

def cleaner(temp_data):

    if len(temp_data.columns) > 8:
        over_columns = [temp_data.columns[8:len(temp_data.columns)]]
        temp_data.drop(over_columns[0], inplace=True, axis=1)
    
    columns = [temp_data.columns[1:len(temp_data.columns)]]
    if 'Unnamed' in str(columns):
        newColumns = temp_data.loc[0].tolist()
        temp_data.columns = newColumns
    
    columns = [temp_data.columns[1:len(temp_data.columns)]]
    if 'IBGE' in str(columns):
        temp_data = temp_data.drop(['IBGE'], axis=1)      

    i=0
    while len(temp_data.columns) < 8:
        temp_data['NaN{}'.format(i)] = np.nan
        i+=1
    
    temp_data = temp_data.dropna(how='all')
    
    arr = temp_data[1:].values

    head = [
        "REGIONAL",
        "MUNICIPIO",
        "CONFIRMADOS",
        "OBITOS",
        "DESCARTADOS",
        "INVESTIGACAO",
        "TOTAL",
        "DATA"
    ]

    dataset = pd.DataFrame(data=arr,
                          columns=head)
            
    dataset['REGIONAL'] = dataset['REGIONAL'].fillna(0)   
    dataset['REGIONAL'] = pd.to_numeric(dataset['REGIONAL'], errors='coerce')
    dataset.dropna(subset=['REGIONAL'], inplace=True)

    dataset.dropna(subset=['MUNICIPIO'], inplace=True)
    dataset['MUNICIPIO'] = dataset['MUNICIPIO'].str.title()
    dataset = dataset[~dataset.MUNICIPIO.str.contains("/|Total|Fora", na=False)]
    
    dataset['CONFIRMADOS'] = pd.to_numeric(dataset['CONFIRMADOS'], errors='coerce')
    dataset.dropna(subset=['CONFIRMADOS'], inplace=True)
    
    dataset['DESCARTADOS'] = pd.to_numeric(dataset['DESCARTADOS'], errors='coerce')

    dataset['INVESTIGACAO'] = pd.to_numeric(dataset['INVESTIGACAO'], errors='coerce')

    return dataset

def catcher():
    
    dataset = pd.DataFrame()
    temp_dataset = pd.DataFrame()
    
    date = datetime.now().date()
    firstCase = datetime(2020, 4, 16).date()

    while formatDate(2, date) != formatDate(2, firstCase):
        r = requests.get('http://www.saude.pr.gov.br/arquivos/File/INFORME_EPIDEMIOLOGICO_{}.csv'.format(formatDate(4, date)))
        r.raise_for_status

        while not r.ok:
            date = getPreviousDate(date)

            r = requests.get('http://www.saude.pr.gov.br/arquivos/File/INFORME_EPIDEMIOLOGICO_{}.csv'.format(formatDate(4, date)))
            r.raise_for_status
        
        else: 
            url = ("http://www.saude.pr.gov.br/arquivos/File/INFORME_EPIDEMIOLOGICO_{}.csv").format(formatDate(4, date))
            temp_dataset = pd.read_csv(url, sep=',|;', engine='python', error_bad_lines=False, encoding='ISO-8859-1')
            
            temp_dataset = cleaner(temp_dataset)
           
            temp_dataset['DATA'] = date

        dataset = pd.concat([dataset, temp_dataset])
        
        date = getPreviousDate(date)

    dataset.reset_index(drop=True, inplace=True)

    dataset.insert(len(dataset.columns), "insert_date", now())
    
    return dataset

def insertData(session):

    print("Coletando e inserindo dados para SESA-base-Paraná...")

    dataset = catcher()
    
    dbFormat = tableClass.SESA_parana()

    dataset.to_sql('SESA_base_PR', con=session.get_bind(), index_label='id', if_exists='replace', method='multi', chunksize=50000, dtype=dbFormat)

    return ''



