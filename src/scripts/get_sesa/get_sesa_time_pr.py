from scripts.functions import now
from database import sql_creator
from sqlalchemy.types import String, Date, Integer, Float, DateTime
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import requests
import tabula
import os
 
#start  ->  end     ->  status  ->  issues
#17-4   ->  21-4    ->  ok      ->  Nothing
#22-4   ->  12-5    ->  ok      ->  30/4 url issue. 2020/05 not 2020/04 at first {} field
#13-5   ->  26-5    ->  ok      ->  Nothing
#27-5   ->  hoje    ->  ok      ->  Nothing

def transform(dfs):
    
    for df in dfs:
        # print(dfs[df])
        try:
            dfs[df] = dfs[df].str.replace(".","").astype(int)
        except:
            pass

    return dfs 

def templateSelector(start_date):

    dirname = os.path.dirname(__file__)
    if start_date <= datetime(2020, 4, 21, 14, 0, 0).date():
        template_path = os.path.join(dirname, r'./templates/17-04.json')
    elif start_date <= datetime(2020, 5, 12, 14, 0, 0).date():
        template_path = os.path.join(dirname, r'./templates/22-04.json')
    elif start_date <= datetime(2020, 5, 26, 14, 0, 0).date():
        template_path = os.path.join(dirname, r'./templates/13-05.json')
    else:
        template_path = os.path.join(dirname, r'./templates/27-05.json')

    print(template_path)
    return template_path

def insert(session):

    print("Inserindo SESA_time_PR")
    data_check = False
    complements = ['_', '%20', '_atualizado', '_1', '_0', '']
    prefixes = ['', '_']
    texto = 'informe_epidemiologico'
    base_url = 'http://www.saude.pr.gov.br/sites/default/arquivos_restritos/files/documento/{}/{}{}_{}{}.pdf'
    final_df = pd.DataFrame()

    try:
        selectObj = sql_creator.Select(session)
        start_date = selectObj.Date('date', '"SESA_time_PR"') # DATABASE DATE
        start_date += timedelta(days=1)
        print("Data has been found, start date is ", start_date)
    except:
        start_date = datetime(2020, 4, 17, 14, 0, 0).date()    
        print("No data found, start date is ", start_date)
    
    # TEST DATE
    # start_date = datetime(2020, 4, 29, 14, 0, 0).date()
    # hoje = datetime(2020, 5, 1, 14, 0, 0).date()

    hoje = now().date()

    while start_date <= hoje:
        if start_date != datetime(2020, 4, 30, 14, 0, 0).date():
            for pfx in prefixes:
                for com in complements:
                    url = base_url.format(start_date.strftime('%Y-%m'), pfx, texto, start_date.strftime('%d_%m_%Y'), com)
                    response = requests.get(url) # url com texto em lowercase
                    # print(url)
                    if response.ok: # se True
                        print("COMPLEMENTO = ", com)
                        print("link do dia ", start_date.strftime("%d-%m"))
                        print(url)
                        data_check = True
                        break # quebra loop complements
                    else: # senão, 
                        url = base_url.format(start_date.strftime('%Y-%m'), pfx, texto.upper(), start_date.strftime('%d_%m_%Y'), com)
                        response = requests.get(url) # url com texto em uppercase
                        # print(url)
                        if response.ok: # se True
                            print("COMPLEMENTO = ", com)
                            print("link do dia ", start_date.strftime("%d-%m"))
                            print(url)
                            data_check = True
                            break # quebra loop complements
       
                if response.ok:
                    break # quebra loop pfx in prefixes
                
        else: # 30/04 url issue -> /2020-05/informe_epidemiologico_30_04_2020_0.pdf"
            url = "http://www.saude.pr.gov.br/sites/default/arquivos_restritos/files/documento/2020-05/informe_epidemiologico_30_04_2020_0.pdf"
            print(url)

        if not response.ok:
            if not data_check:
                print("get_sesa_leitos sem boletim")
            break
        
        template_path = templateSelector(start_date)
        df = tabula.read_pdf_with_template(url, template_path, pandas_options={'header': None, 'dtype': str})

        temp_df = pd.DataFrame([[df[0][0][1], df[0][0][2]]], columns=['cases', 'deaths'])
       
        temp_df = transform(temp_df)
        temp_df['date'] = start_date
        print(temp_df)
        final_df = pd.concat([final_df, temp_df], ignore_index=True)

        start_date += timedelta(days=1)

    if data_check: 
        final_df.to_sql("SESA_time_PR", index=False, con=session.get_bind(), if_exists='append', method='multi',
        dtype={
            'cases': Integer(),
            'deaths': Integer(),
            'date': Date()
        })
        print("sesa_time_pr inserido com sucesso")
    
    else:
        print("sesa_time_pr está atualizado")