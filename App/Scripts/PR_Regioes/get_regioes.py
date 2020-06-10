import pandas as pd

def catcher():

    url = ('https://docs.google.com/spreadsheets/d/1YW7wzx0bxIoM9AdZd14SYCD0bv7ZI3wy6AYFdv-AfvU/export?gid=0&format=csv')
    dataset = pd.read_csv(url, encoding='utf-8', engine='python', error_bad_lines=False)

    return dataset

def insertData(session):

    dataset = catcher()

    dataset.to_sql('PR_base_regioes', con=session.get_bind(), index_label='id', if_exists='replace', method='multi', chunksize=50000)

    return ''