from Scripts.functions import now, urlGenerator, getApi, getNextDate, formatDate
from DataBase import sqlCreator
from sqlalchemy.types import String, Date, Integer, Float
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import requests
import tabula

mcroaa_columns = [
    'reg saude',
    'municipio',
    'pop',
    'confirmados',
    'recuperados',
    'obitos',
    'investigacao'
]

def transform(dfs):


    dfs.loc['Total' ] = '0'
    for col in mcroaa_columns:
        try:
            dfs[col] = dfs[col].str.replace(".", "").astype(int)
            dfs.loc['Total', col] = dfs[col].sum()
        except:
            pass 
        
    
    dfs.loc['Total', 'reg saude'] = ''
    dfs.loc['Total', 'municipio'] = ''
    dfs.dropna(inplace=True)

    return dfs

def cleanner(d):
        
    # if len(d.keys()) == 2: # 
           
    #     new_d = []
    #     d.drop(columns=[0], inplace=True)
    #     raw_data = d[5:].values.tolist() # avaliar maneira do 3 virar variavel
    #     for raw in raw_data:
    #         new_line = []   
    #         r1 = raw[0].split(' ', 1)
    #         new_line.append(r1[0])
    #         r2 = r1[1].rsplit(' ', 5)
    #         for r in r2:
    #             new_line.append(r)
    #         new_d.append(new_line)
    #     d = pd.DataFrame(new_d)
    #     d.columns = mcroaa_columns
    
    if len(d) > 5:
        drop = 1

        try:
            d[0] = pd.DataFrame(d[0].str.replace(" ", "").values)
            d.dropna(axis='columns', how='all', inplace=True)
            for i in range(len(d)):
                number = d.loc[i, 0]
                if len(number) > 5:
                    d.loc[i, 0] = number[-2:] # RS
                    fill_value = number[0:-5] # valor pra da fill
                    # print(number, fill_value, type(d.iloc[i, 3]))
                    d.loc[i] = d.loc[i].fillna(fill_value, axis=0)
                    drop = 0
                elif len(number) > 3:
                    d.loc[i, 0] = number[-2:]
                    drop = 0
        except:
            pass

        # if len(d.keys()) == 8:
        #     new_d = []
        #     drop = 1

        #     try:
        #         new_0 = pd.DataFrame(d[0].str.split(' ').values.tolist())
        #         # print(new_0)
        #         if len(new_0.iloc[1]) > 1:
        #             drop = 0
        #             d[0] = new_0[1]
        #             d.dropna(axis='columns', how='all', inplace=True)
        #             df.fillna(0)
        #     except:
        #         pass

        try:
            d.loc[d[0] == '115', 2] = 'Nova Esperança do Sudoeste'
            d.dropna(inplace=True)    
        except:
            pass
        
        if drop == 1:
            d.drop(columns=[0], inplace=True)
        
        d.columns = mcroaa_columns

    return d

def get_data(session, page_list):
    

    texto = 'informe_epidemiologico'
    base_url = 'http://www.saude.pr.gov.br/sites/default/arquivos_restritos/files/documento/{}/{}_{}.pdf'

    # hoje = now()
    hoje = datetime(2020, 6, 19, 19, 0, 0)
    url = base_url.format(hoje.strftime('%Y-%m'), texto, hoje.strftime('%d_%m_%Y'))
    response = requests.get(url)
    
    df = pd.DataFrame()

    if not response.ok:
        url = base_url.format(hoje.strftime('%Y-%m'), texto.upper(), hoje.strftime('%d_%m_%Y'))
        response = requests.get(url)

    if not response.ok:
        print("erro link")
    else:

        df = tabula.read_pdf(url, pages=page_list, pandas_options={'header': None, 'dtype': str})

        dfs = pd.DataFrame()

        # page by page
        print("CRIANDO DIA = ", hoje.strftime("%d-%m"))
        with pd.ExcelWriter('SESA_FULL.xlsx') as writer: #salva pré processamento dos dados
            i = 15
            for d in range(len(df)):
                df[d].to_excel(writer, index=False, engine='xlsxwriter', encoding='UTF-8', sheet_name='PG-{}'.format(i))
                i+=1

        for d in df:
            # print(d)
            d = cleanner(d)
            if len(d.keys()) == 7:
                # d = transform(d)
                dfs = pd.concat([dfs, d])
    
        dfs = transform(dfs)
        dfs['date'] = hoje
        # Full data
        print("CRIANDO Clean DIA = ", hoje.strftime("%d-%m"))
        with pd.ExcelWriter('SESA_FULL-Clean.xlsx') as writer:
            dfs.to_excel(writer, index=False, engine='xlsxwriter', encoding='UTF-8', sheet_name='SESA_FULL')

        dfs.to_sql('SESA_base_PR', con=session.get_bind(), if_exists='replace', method='multi',
        dtype={
            'REGIONAL': String(),
            'MUNICIPIO': String(),
            'POPULACOA': Integer(),
            'CONFIRMADOS': Integer(),
            'RECUPERADOS': Integer(),
            'OBITOS': Integer(),
            'INVESTIGACAO': Integer(),
            'DATE': Date()
        })
    
    return ''