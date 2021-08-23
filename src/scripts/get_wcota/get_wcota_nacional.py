import pandas as pd
from database import sql_creator
from database import table_class
from scripts.functions import now
from datetime import datetime, timedelta

def cleaner(dataset, is_first):

    if is_first:
        dataset = dataset[~dataset.state.str.contains("TOTAL", na=False)]
        dataset.drop(columns=["epi_week"], inplace=True)
    
    dataset.drop(columns=["country", "_source", "last_info_date"], inplace=True)
    
    return dataset

def insert(session):

    print("Inserindo get_wcota_nacional.")
    db_format = table_class.WCota_nacional()

    try:
        selectObj = sql_creator.Select(session)
        last_date = selectObj.Date('date', '"WCota_base_nacional"') # DATABASE DATE
        print("Data has been found, last_date\t", last_date)
        
        # url = ("https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities.csv")
        # dataset = pd.read_csv(url, encoding='utf-8', engine='python', error_bad_lines=False)
        
        # df_date = datetime.strptime(dataset["date"][0], '%Y-%m-%d').date()
        last_date += timedelta(days=1)
        print("LAST", last_date)
        
        if last_date < now().date():
            print("Atrasado")
            is_first = True
        else:
            is_first = False

    except:
        print("No data found.")
        #EXECUTA O SHELL DE DOWNLOAD E DESCOMPACTACAO DO ARQUIVO.
        # dataset = pd.read_csv('~/cases-brazil-cities-time.csv')

        # url = ("https://github.com/wcota/covid19br/raw/master/cases-brazil-cities-time.csv.gz")
        # dataset = pd.read_csv(url, compression='gzip')
           
        is_first = True
        # print(dataset)
        
    # dataset = cleaner(dataset, is_first)
    # dataset["date"][0] = "2021-08-07"
    # print("Dataset date\t\t\t", dataset["date"][0])
    if is_first:
        print("Huge data volume is comming.")
        url = ("https://github.com/wcota/covid19br/raw/master/cases-brazil-cities-time.csv.gz")
        dataset = pd.read_csv(url, compression='gzip')
        dataset = cleaner(dataset, is_first)

        dataset.to_sql('WCota_base_nacional', con=session.get_bind(),
                    index=False, if_exists='replace', method='multi',
                    chunksize=50000, dtype=db_format)
    else:  

        print("Inserindo dados do dia", last_date)
        url = ("https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities.csv")
        dataset = pd.read_csv(url, encoding='utf-8', engine='python', error_bad_lines=False)
        
        if datetime.strptime(dataset["date"][0], '%Y-%m-%d').date() > last_date:
            print(dataset)  

            dataset.to_sql('WCota_base_nacional', con=session.get_bind(),
                    index=False, if_exists='append', method='multi',
                    chunksize=50000, dtype=db_format)
                    
            print("Base se encontra atualizada !")

    return print("wcota_nacional inserido com sucesso!")
