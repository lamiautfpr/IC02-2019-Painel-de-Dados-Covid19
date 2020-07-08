import pandas as pd
from scripts.functions import url_generator, get_api, next_date, format_date, now
from database import sql_creator
from datetime import datetime


def catcher(date):
    df = pd.DataFrame()

    today = now()

    while date < today:
        url = 'https://covid19-brazil-api.now.sh/api/report/v1/brazil/{}'.format(format_date(1, date))
        content = get_api(url)
        df = df.append(content, ignore_index=True)
        date = next_date(date)
    return df


def insert(session):
    print("Inserindo get_brapi_nacional.")
    
    select_date = sql_creator.Select(session)
    try:
        date = format_date(2, select_date.Date('datetime', '"Brasil_api_base_nacional"'))
    except:
        date = datetime(2020, 3, 18)

    dataset = catcher(date)
    dataset.to_sql('Brasil_api_base_nacional', con=session.get_bind(),
                   index_label='id', if_exists='append', method='multi',
                   chunksize=50000)
    return print("brapi_nacional inserido com sucesso!")
