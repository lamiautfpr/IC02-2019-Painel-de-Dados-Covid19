from Scripts.functions import now
from datetime import datetime
from DataBase import tableClass
import pandas as pd

def cleaner(temp_dataset):
    
    temp_dataset = temp_dataset.drop(columns=['Unnamed: 0', 'Unnamed: 2', 'Fonte'], axis=1)
    
    temp_dataset = temp_dataset[~temp_dataset.UF.str.contains("LEITOS", na=False)]

    arr = temp_dataset[0:].values

    head = [
        "UF",
        "leitosOcupados",
        "quantidadeLeitos",
        "totalOcupacao",
        "ultimaAtualizacao"
    ]

    dataset = pd.DataFrame(data=arr,
                          columns=head)

    dataset['leitosOcupados'] = pd.to_numeric(dataset['leitosOcupados'], errors='coerce')
    
    dataset['quantidadeLeitos'] = pd.to_numeric(dataset['quantidadeLeitos'], errors='coerce')

    dataset['totalOcupacao'] = (dataset['leitosOcupados']/dataset['quantidadeLeitos'])*100

    dataset['ultimaAtualizacao'] = dataset['ultimaAtualizacao'] + "/2020"
    dataset['ultimaAtualizacao'] = pd.to_datetime(dataset.ultimaAtualizacao, format='%d/%m/%Y')

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

    dbFormat = tableClass.WCota_leitos()

    dataset = catcher()
    
    dataset.to_sql('WCota_base_leitos', con=session.get_bind(), index_label='id', if_exists='append', method='multi', chunksize=50000, dtype=dbFormat)
    
    return ''