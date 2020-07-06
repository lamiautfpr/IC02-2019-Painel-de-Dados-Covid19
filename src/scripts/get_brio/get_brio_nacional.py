import io
import gzip
import pandas as pd
from database import table_class
from scripts.functions import now
from urllib.request import Request, urlopen


def catcher():
    req = Request('https://data.brasil.io/dataset/covid19/caso_full.csv.gz', 
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu;Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
            'Accept-Encoding': 'gzip'
            })
    response = urlopen(req)
    content = gzip.decompress(response.read())

    dataset = pd.read_csv(io.StringIO(content.decode('utf-8')))
    dataset.insert(len(dataset.columns), "insert_date", now())
    return dataset


def insert(session):
    print("Inserindo get_brio_nacional.")

    db_format = table_class.Brasil_io_nacional()
    dataset = catcher()
    
    dataset.to_sql('Brasil_io_base_nacional', con=session.get_bind(), 
                    index_label='id', if_exists='replace', method='multi', 
                    chunksize=50000, dtype=db_format)
    return print("brio_nacional inserido com sucesso!")