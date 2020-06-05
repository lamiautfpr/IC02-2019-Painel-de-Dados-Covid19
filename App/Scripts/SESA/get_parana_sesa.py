from Scripts.functions import now
from datetime import datetime, timedelta
from DataBase import tableClass
import pandas as pd
import numpy as np
import requests

def getDate(i):

    date = datetime.now() - timedelta(i)
    date = date.strftime('%Y/%m/%d')

    return date

def formatDate(date):

    datetimeobject = datetime.strptime(date,"%Y/%m/%d")
    date = datetimeobject.strftime('%d_%m_%Y')

    return date

def cleaner(temp_data):

    #Remove over columns
    if len(temp_data.columns) > 8:
        over_columns = [temp_data.columns[8:len(temp_data.columns)]]
        temp_data.drop(over_columns[0], inplace=True, axis=1)
    
    #Remove title
    columns = [temp_data.columns[1:len(temp_data.columns)]]
    if 'Unnamed' in str(columns):
        newColumns = temp_data.loc[0].tolist()
        temp_data.columns = newColumns
    
    #Remove IBGE column
    columns = [temp_data.columns[1:len(temp_data.columns)]]
    if 'IBGE' in str(columns):
        temp_data = temp_data.drop(['IBGE'], axis=1)      

    #Insert missing columns
    i=0
    while len(temp_data.columns) < 8:
        temp_data['NaN{}'.format(i)] = np.nan
        i+=1
    
    #Drop all null rows
    temp_data = temp_data.dropna(how='all')
    
    #Get the cell's values without labels
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

    #Insert values into dataset with new labels
    dataset = pd.DataFrame(data=arr,
                          columns=head)

    #Fill NaN to 0 in Regional de Saude                          
    dataset['REGIONAL'] = dataset['REGIONAL'].fillna(0)   
    #Insert NaN to error values and drop row in Regional de Saude 
    dataset['REGIONAL'] = pd.to_numeric(dataset['REGIONAL'], errors='coerce')
    dataset.dropna(subset=['REGIONAL'], inplace=True)

    #Drop NaN values in Municipio
    dataset.dropna(subset=['MUNICIPIO'], inplace=True)
    
    #Insert NaN to error values and drop row in Confirmados
    dataset['CONFIRMADOS'] = pd.to_numeric(dataset['CONFIRMADOS'], errors='coerce')
    dataset.dropna(subset=['CONFIRMADOS'], inplace=True)

    #Fill /|Total|Fora and drop row in Municipio
    dataset = dataset[~dataset.MUNICIPIO.str.contains("/|Total|Fora", na=False)]
    
    return dataset

def catcher():
    
    date = formatDate(getDate(0))
    r = requests.get('http://www.saude.pr.gov.br/arquivos/File/INFORME_EPIDEMIOLOGICO_{}.csv'.format(date))
    r.raise_for_status

    i=1
    while not r.ok:
        date = formatDate(getDate(i))
        r = requests.get('http://www.saude.pr.gov.br/arquivos/File/INFORME_EPIDEMIOLOGICO_{}.csv'.format(date))
        r.raise_for_status
        i+=1

    url = ("http://www.saude.pr.gov.br/arquivos/File/INFORME_EPIDEMIOLOGICO_{}.csv").format(date)
    dataset = pd.read_csv(url, sep=',|;', encoding='ISO-8859-1', engine='python', error_bad_lines=False)
    
    dataset = cleaner(dataset)

    dataset['DATA'] = getDate(i-1)
    
    dataset.insert(len(dataset.columns), "insert_date", now())
    
    return dataset

def insertData(session):

    print("Coletando e inserindo dados para SESA-base-Paraná...")

    dataset = catcher()
    
    dbFormat = tableClass.SESA_parana()

    dataset.to_sql('SESA_base_PR', con=session.get_bind(), index_label='id', if_exists='replace', method='multi', chunksize=50000, dtype=dbFormat)

    return ''