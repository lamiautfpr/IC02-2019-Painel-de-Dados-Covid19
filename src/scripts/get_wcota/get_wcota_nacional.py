import pandas as pd
from database import table_class
from scripts.functions import now


def cleaner(dataset):
    dataset = dataset[~dataset.state.str.contains("TOTAL", na=False)]
    dataset = dataset.sort_values(by='date', ascending=False)
    dataset.reset_index(drop=True, inplace=True)
    return dataset


def catcher():
    url = ("https://github.com/wcota/covid19br/blob/master/cases-brazil-cities-time.csv.gz?raw=true")
    dataset = pd.read_csv(url, encoding='utf-8',
                          engine='python', error_bad_lines=False, compression='gzip')

    dataset = cleaner(dataset)

    dataset.insert(len(dataset.columns), "insert_date", now())
    return dataset


def insert(session):
    print("Inserindo get_wcota_nacional.")

    db_format = table_class.WCota_nacional()
    dataset = catcher()

    dataset.to_sql('WCota_base_nacional', con=session.get_bind(),
                   index_label='id', if_exists='replace', method='multi',
                   chunksize=50000, dtype=db_format)
    return print("wcota_nacional inserido com sucesso!")
