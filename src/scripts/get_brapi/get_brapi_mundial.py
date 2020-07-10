import pandas as pd
from database import table_class
from scripts.functions import now, get_api


def catcher():
    url = 'https://covid19-brazil-api.now.sh/api/report/v1/countries'
    content = get_api(url)

    df = pd.DataFrame(content)
    df.insert(len(df.columns), "insert_date", now())
    return df


def insert(session):
    print("Inserindo get_brapi_mundo.")

    df = catcher()
    df.to_sql('Brasil_api_base_mundo', con=session.get_bind(),
                   index_label='id', if_exists='replace', method='multi',
                   chunksize=10000)
    return print("brapi_mundial inserido com sucesso!")
