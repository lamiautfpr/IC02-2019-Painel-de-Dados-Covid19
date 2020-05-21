from DataBase import tableClass
import pandas as pd

def cleaner(dataset):

    dataset = dataset[~dataset.state.str.contains("TOTAL", na=False)]
    
    dataset = dataset.sort_values(by='date', ascending=False)

    dataset.reset_index(drop=True, inplace=True)

    return dataset

def catcher():

    url = ("https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities-time.csv")
    dataset = pd.read_csv(url, encoding='utf-8', engine='python', error_bad_lines=False)
    
    dataset = cleaner(dataset)

    return dataset

def insertData(session):

    dbFormat = tableClass.WCota_nacional()

    dataset = catcher()
    
    dataset.to_sql('WCota_base_nacional', con=session.get_bind(), index_label='id', if_exists='replace', method='multi', dtype=dbFormat)
    
    return ''