from Scripts.functions import now        
from urllib.request import Request, urlopen
from DataBase import tableClass
import pandas as pd

def catcher():

    req = Request('https://brasil.io/dataset/covid19/obito_cartorio/?format=csv')
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0')
    content = urlopen(req)

    dataset = pd.read_csv(content)

    dataset.insert(len(dataset.columns), "insert_date", now())

    return dataset

def insertData(session):

    print("Coletando e inserindo dados para Brasil-io-base-cartorio...")

    dbFormat = tableClass.Brasil_io_cartorio()

    dataset = catcher()
    
    dataset.to_sql('Brasil_io_base_cartorio', con=session.get_bind(), index_label='id', if_exists='append', method='multi', chunksize=50000, dtype=dbFormat)
    
    return ''
