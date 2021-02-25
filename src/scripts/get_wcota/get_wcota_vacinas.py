import pandas as pd
from database import table_class
from scripts.functions import now


def cleaner(dataset):

    dataset.drop(dataset[dataset.state == 'TOTAL'].index, inplace=True)
    dataset.drop(columns=['epi_week','country', 'city', 'newDeaths', 'deaths', 'newCases',
        'totalCases', 'deathsMS', 'totalCasesMS', 'deaths_per_100k_inhabitants', 
        'totalCases_per_100k_inhabitants', 'deaths_by_totalCases', 'recovered'], inplace=True)
    # print(dataset[dataset['state'] == 'TOTAL'])
    dataset.columns = ['Data', 'Estado', 'Suspeitos', 'Testes', 'Testes_100k', 'Vacinados', 'Vacinados_100k', 'Segunda_Dose', 'Segunda_Dose_100k']
    
    dataset['Testes_100k'] = round(dataset['Testes_100k'], 2)
    dataset['Vacinados_100k'] = round(dataset['Vacinados_100k'], 2)


    return dataset

 
def catcher():

    # https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv

    url = ("https://raw.githubusercontent.com/wcota/"
           "covid19br/master/cases-brazil-states.csv")
    
    dataset = pd.read_csv(url, delimiter=',', encoding='utf-8', engine='python', error_bad_lines=False)

    print(dataset)

    dataset = cleaner(dataset)

    print(dataset)

    # dataset.info()

    return dataset


def insert(session):

    print("Inserindo get_wcota_vacinas.")

    db_format = table_class.WCota_vacinas()
    dataset = catcher()

    dataset.to_sql('WCota_Vacinas_Estados', con=session.get_bind(),
                   index=False, if_exists='replace', method='multi',
                   chunksize=50000, dtype=db_format)

    return print("WCota_vacinas inserido com sucesso!")
