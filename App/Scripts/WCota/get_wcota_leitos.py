from Scripts.functions import now
from DataBase import tableClass
import pandas as pd

def cleaner(dataset):
    
    dataset = dataset.drop(columns=['Unnamed: 0', 'Unnamed: 2', 'Fonte'], axis=1)
    
    dataset = dataset[~dataset.UF.str.contains("LEITOS", na=False)]

    dataset = dataset.dropna(how='all')

    return dataset

def catcher():

    url = ("https://docs.google.com/spreadsheets/d/1MWQE3s4ef6dxJosyqvsFaV4fDyElxnBUB6gMGvs3rEc/export?gid=235349683&format=csv")
    dataset = pd.read_csv(url, encoding='utf-8', engine='python', error_bad_lines=False)
    
    dataset = cleaner(dataset)
    
    dataset.insert(len(dataset.columns), "insert_date", now())

    return dataset

def insertData(session):

    print("Coletando e inserindo dados para WCota-base-leitos...")

    dataset = catcher()
    
    dataset.to_sql('WCota_base_leitos', con=session.get_bind(), index_label='id', if_exists='replace', method='multi', chunksize=50000)
    
    return ''