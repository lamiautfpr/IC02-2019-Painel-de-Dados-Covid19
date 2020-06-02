from Scripts.functions import now
from DataBase import tableClass
import pandas as pd

def cleaner(dataset):

    dataset = dataset.sort_values(by='data', ascending=False)

    dataset.reset_index(drop=True, inplace=True)

    return dataset

def catcher():

    url = ("C:/Users/guiyo/Documents/GitHub/IC02-2019-Painel-de-Dados-Covid19/arquivo_srag.csv")
    dataset = pd.read_csv(url, encoding='utf-8', engine='python', error_bad_lines=False, sep=';')
    
    dataset = cleaner(dataset)
    
    dataset.insert(len(dataset.columns), "insert_date", now())

    return dataset

def insertData(session):

    print("Coletando e inserindo dados para SRAG-Covid-Brazil...")

    dataset = catcher()
    
    dataset.to_sql('SRAG_base_nacional', con=session.get_bind(), index_label='id', if_exists='replace', method='multi', chunksize=50000)
    
    return ''