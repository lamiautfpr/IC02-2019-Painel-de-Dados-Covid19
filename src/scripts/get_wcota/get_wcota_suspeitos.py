import pandas as pd
from database import table_class
from scripts.functions import now


def cleaner(temp_dataset):
    temp_dataset = temp_dataset.drop(temp_dataset.index[30:])
    temp_dataset = temp_dataset.drop(columns=[',', 'Unnamed: 9', 'Unnamed: 10'], axis=1)

    arr = temp_dataset[3:].values
    head = [
        "Estado",
        "Casos",
        "Suspeitos",
        "Recuperados",
        "Obitos",
        "Testes",
        "novosCasos",
        "novosObitos"
    ]
    dataset = pd.DataFrame(data=arr,
                           columns=head)

    dataset['Suspeitos'] = pd.to_numeric(dataset['Suspeitos'], errors='coerce')
    dataset['Recuperados'] = pd.to_numeric(dataset['Recuperados'], errors='coerce')
    dataset['Testes'] = pd.to_numeric(dataset['Testes'], errors='coerce')
    return dataset


def catcher():
    url = ("https://docs.google.com/spreadsheets/d/"
           "1MWQE3s4ef6dxJosyqvsFaV4fDyElxnBUB6gMGvs3rEc"
           "/export?gid=1503196283&format=csv")
    dataset = pd.read_csv(url, encoding='utf-8',
                          engine='python', error_bad_lines=False)

    dataset = cleaner(dataset)
    dataset.insert(len(dataset.columns), "insert_date", now())
    return dataset


def insert(session):
    print("Inserindo get_wcota_suspeitos.")

    db_format = table_class.WCota_suspeitos()
    dataset = catcher()

    dataset.to_sql('WCota_base_suspeitos', con=session.get_bind(),
                   index_label='id', if_exists='replace', method='multi',
                   chunksize=50000, dtype=db_format)
    return print("wcota_suspeitos inseridos com sucesso!")
