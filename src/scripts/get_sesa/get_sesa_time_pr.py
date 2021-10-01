from scripts.functions import now
from database import sql_creator
from sqlalchemy.types import String, Date, Integer, Float, DateTime
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import requests
import tabula
import os
 

def transform(dfs):
    
    for df in dfs:
        # print(dfs[df])
        try:
            dfs[df] = dfs[df].str.replace(".","").astype(int)
        except:
            pass

    return dfs 

def clean_WLD(dfs, start_date):

    for df in dfs:
        dfs[df] = dfs[df].str.replace(" ", "")
        dfs[df] = dfs[df].str.replace(".","")

        if len(dfs) == 4:
            dfs.dropna(inplace=True)

        if start_date.month == 3:
            if start_date.day >= 30:
                dfs[df].iloc[2] = dfs[df].iloc[2][:3] + dfs[df].iloc[2][(3+1):] # 3
                dfs[df].iloc[2] = dfs[df].iloc[2][:4] + dfs[df].iloc[2][(4+3):] # 4->7
                dfs[df].iloc[2] = dfs[df].iloc[2][:5] + dfs[df].iloc[2][(5+1):] # 6 


    return dfs

def clean_BR(dfs, start_date):

    for df in dfs:
        
        print("DF com ",len(dfs), "linhas")
        # print(dfs[df])
        # dfs[df] = dfs[df].str.replace(" ", "")
        # dfs[df] = dfs[df].str.replace(".","")

       # if start_date.month == 3: #< datetime(2021, 4, 6, 14, 0, 0).date():
        if len(dfs[df]) == 4:
            dfs[df] = dfs[df].str.replace(" ", "")
            dfs[df] = dfs[df].str.replace(".","")
            if start_date.month == 4:
                if (start_date.day > 11 and start_date.day < 15) or (start_date.day == 17):
                    dfs[df].iloc[-1] = dfs[df].iloc[-1][:3] + dfs[df].iloc[-1][(3+1):]
                    dfs[df].iloc[-1] = dfs[df].iloc[-1][:4] + dfs[df].iloc[-1][(4+1):]
                else:
                    if start_date.day != 4 and start_date.day != 5:
                        dfs[df].iloc[-1] = dfs[df].iloc[-1][:4] + dfs[df].iloc[-1][(4+1):]
                        dfs[df].iloc[-1] = dfs[df].iloc[-1][:4] + dfs[df].iloc[-1][(4+1):]

                #clean row indexed by number [1]
                dfs[df].dropna(inplace=True)
                dfs[df].iloc[1] = dfs[df].iloc[1][:5] + dfs[df].iloc[1][(5+1):]
                dfs[df].iloc[1] = dfs[df].iloc[1][:5] + dfs[df].iloc[1][(5+1):]

            elif start_date.month == 5:
                if start_date.day >= 27 and start_date.day < 30:
                    dfs[df].iloc[1] = dfs[df].iloc[1][:5] + dfs[df].iloc[1][(5+1):]
                else:
                    dfs[df].iloc[1] = dfs[df].iloc[1][:5] + dfs[df].iloc[1][(5+1):]
                    dfs[df].iloc[1] = dfs[df].iloc[1][:5] + dfs[df].iloc[1][(5+1):]
                    if start_date.day < 27:
                        if start_date.day == 7:
                            dfs[df].iloc[-1] = dfs[df].iloc[-1][:4] + dfs[df].iloc[-1][(4+1):]
                            dfs[df].iloc[-1] = dfs[df].iloc[-1][:4] + dfs[df].iloc[-1][(4+1):]
                        else:
                            dfs[df].iloc[-1] = dfs[df].iloc[-1][:3] + dfs[df].iloc[-1][(3+1):]
                            dfs[df].iloc[-1] = dfs[df].iloc[-1][:4] + dfs[df].iloc[-1][(4+1):]
            
            elif start_date.month == 6:
                dfs[df].iloc[1] = dfs[df].iloc[1][:5] + dfs[df].iloc[1][(5+1):]
                dfs[df].iloc[-1] = dfs[df].iloc[-1][:4] + dfs[df].iloc[-1][(4+1):] 
            
            else:
                print("4 linha") #drop row 2
                dfs[df].dropna(inplace=True)
                dfs[df].iloc[1] = dfs[df].iloc[1][:5] + dfs[df].iloc[1][(5+1):]
                dfs[df].iloc[1] = dfs[df].iloc[1][:5] + dfs[df].iloc[1][(5+1):]
            dfs.drop([2], inplace=True)


        if len(dfs[df]) == 5:
            print("5 linha") # drop row 1-3
            dfs[df] = dfs[df].str.replace(" ", "")
            dfs[df] = dfs[df].str.replace(".","")


            if (start_date != datetime(2021, 3, 12, 14, 0, 0).date() and start_date < datetime(2021, 3, 27, 14, 0, 0).date()) or (start_date >= datetime(2021, 4, 1, 14, 0, 0).date() and start_date < datetime(2021, 4, 6, 14, 0, 0).date()):
                dfs[df].iloc[-1] = dfs[df].iloc[-1][:3] + dfs[df].iloc[-1][(3+1):]
                dfs[df].iloc[-1] = dfs[df].iloc[-1][:4] + dfs[df].iloc[-1][(4+1):]
                # dfs.drop([1, 3], inplace=True)
            else:
                if start_date.month == 3:
                    dfs[df].iloc[-1] = dfs[df].iloc[-1][:4] + dfs[df].iloc[-1][(4+1):]
                    dfs[df].iloc[-1] = dfs[df].iloc[-1][:4] + dfs[df].iloc[-1][(4+1):]
                
                if start_date.month == 4:
                    dfs[df].iloc[2] = dfs[df].iloc[2][:5] + dfs[df].iloc[2][(5+1):]
                    dfs[df].iloc[2] = dfs[df].iloc[2][:5] + dfs[df].iloc[2][(5+1):]

                if start_date.month == 5:
                    dfs[df].iloc[2] = dfs[df].iloc[2][:4] + dfs[df].iloc[2][(4+1):]
                    dfs[df].iloc[2] = dfs[df].iloc[2][:5] + dfs[df].iloc[2][(5+1):]
                
                if start_date.month == 6:
                    dfs[df].iloc[2] = dfs[df].iloc[2][:5] + dfs[df].iloc[2][(5+1):]

            dfs.drop([1, 3], inplace=True)

        if len(dfs[df]) == 6:
            print("6 linha") # drop row 0-2-4
            
            if start_date.month == 6:
                dfs[df] = dfs[df].str.replace(" ", "")
                dfs[df] = dfs[df].str.replace(".","")
                dfs[df].iloc[-1] = dfs[df].iloc[-1][:4] + dfs[df].iloc[-1][(4+1):] 
                dfs.drop([0, 2, 4], inplace=True)

            elif start_date.month == 5:
                if start_date.day <= 15:
                    dfs[df] = dfs[df].str.replace(" ", "")
                    dfs[df] = dfs[df].str.replace(".","")
                    dfs.drop([1, 3, 4], inplace=True)# 9/5 -> 15
                else:
                    if start_date.day >= 30:
                        dfs[df] = dfs[df].str.replace(" ", "")
                        dfs[df] = dfs[df].str.replace(".","")
                        dfs[df].iloc[-1] = dfs[df].iloc[-1][:4] + dfs[df].iloc[-1][(4+1):] 
                    else:
                        if ' ' in dfs[df].iloc[-1]:
                            dfs[df] = dfs[df].str.replace(" ", "")
                            dfs[df] = dfs[df].str.replace(".","")
                            dfs[df].iloc[-1] = dfs[df].iloc[-1][:3] + dfs[df].iloc[-1][(3+1):] 
                            dfs[df].iloc[-1] = dfs[df].iloc[-1][:4] + dfs[df].iloc[-1][(4+1):] 
                        else:
                            dfs[df] = dfs[df].str.replace(" ", "")
                            dfs[df] = dfs[df].str.replace(".","")
                            dfs[df].iloc[-1] = dfs[df].iloc[-1][:3] + dfs[df].iloc[-1][(3+2):]
                        
                        dfs[df].iloc[3] = dfs[df].iloc[3][:5] + dfs[df].iloc[3][(5+1):] 
                        dfs[df].iloc[3] = dfs[df].iloc[3][:5] + dfs[df].iloc[3][(5+1):] 
                    dfs.drop([0, 2, 4], inplace=True)
   
            else:
                if start_date < datetime(2021, 3, 27, 14, 0, 0).date() or (start_date >= datetime(2021, 4, 19, 14, 0 ,0).date() and start_date <= datetime(2021, 4, 21, 14, 0, 0).date()) or start_date == datetime(2021, 4, 24, 14, 0, 0).date():
                    dfs[df].iloc[-1] = dfs[df].iloc[-1][:3] + dfs[df].iloc[-1][(3+1):]
                    dfs[df].iloc[-1] = dfs[df].iloc[-1][:4] + dfs[df].iloc[-1][(4+1):]
                elif start_date > datetime(2021, 3, 27, 14, 0, 0).date():
                    dfs[df].iloc[-1] = dfs[df].iloc[-1][:4] + dfs[df].iloc[-1][(4+1):]
                    dfs[df].iloc[-1] = dfs[df].iloc[-1][:4] + dfs[df].iloc[-1][(4+1):]
                else:
                    dfs[df].iloc[-1] = dfs[df].iloc[-1][:3] + dfs[df].iloc[-1][(3+1):]
                    dfs[df].iloc[-1] = dfs[df].iloc[-1][:3] + dfs[df].iloc[-1][(3+1):]

                dfs.drop([0, 2, 4], inplace=True)

    dfs.reset_index(drop=True, inplace=True) #reset index
    return dfs

def clean_PR(dfs):

    for df in dfs:
        dfs[df] = dfs[df].str.replace(" ", "")
        dfs[df] = dfs[df].str.replace(".","")
    
    return dfs

def templateSelector(start_date):

    dirname = os.path.dirname(__file__)
    if start_date <= datetime(2020, 4, 21, 14, 0, 0).date():
        template_path = os.path.join(dirname, r'./templates/17-04.json')
    elif start_date <= datetime(2020, 5, 12, 14, 0, 0).date():
        template_path = os.path.join(dirname, r'./templates/22-04.json')
    elif start_date <= datetime(2020, 5, 26, 14, 0, 0).date():
        template_path = os.path.join(dirname, r'./templates/13-05.json')
    elif start_date <= datetime(2021, 2, 12, 14, 0, 0).date():
        template_path = os.path.join(dirname, r'./templates/27-05.json')
    else:
        template_path = os.path.join(dirname, r'./templates/13-02-21.json')
    
    if start_date == datetime(2021, 2, 16, 14, 0, 0).date():
        template_path = os.path.join(dirname, r'./templates/16-02-21.json')
    
    # print(template_path)
   
    return template_path

def insert(session):

    print("Inserindo SESA_time_PR")
    data_check = False
    complements = ['__0', '_', '%20', '_atualizado', '_1', '_0', '']
    prefixes = ['', '_']
    texto = 'informe_epidemiologico'
    base_url = 'http://www.saude.pr.gov.br/sites/default/arquivos_restritos/files/documento/{}/{}{}_{}{}.pdf'
    final_pr = pd.DataFrame()
    final_br = pd.DataFrame()
    final_wld = pd.DataFrame()

    try:
        selectObj = sql_creator.Select(session)
        start_date = selectObj.Date('date', '"SESA_time_PR"') # DATABASE DATE
        start_date += timedelta(days=1)
        print("Data has been found, start date is ", start_date)
    except:
        start_date = datetime(2020, 4, 17, 14, 0, 0).date()    
        print("No data found, start date is ", start_date)
    
    hoje = now().date()
    
    # TEST DATE
    # start_date = datetime(2021, 6, 1, 14, 0, 0).date()
    # hoje = datetime(2021, 6, 8, 14, 0, 0).date()
    
    while start_date <= hoje:
        if start_date != datetime(2021, 4, 1, 14, 0 ,0).date():   
            if start_date != datetime(2020, 4, 30, 14, 0, 0).date():
                if start_date != datetime(2020, 8, 12, 14, 0, 0).date():
                    for pfx in prefixes:
                        for com in complements:
                            url = base_url.format(start_date.strftime('%Y-%m'), pfx, texto, start_date.strftime('%d_%m_%Y'), com)
                            response = requests.get(url) # url com texto em lowercase
                            print(url)
                            if response.ok: # se True
                                # print("COMPLEMENTO = ", com)
                                # print("link do dia ", start_date.strftime("%d-%m"))
                                # print(url)
                                data_check = True
                                break # quebra loop complements
                            else: # senão, 
                                url = base_url.format(start_date.strftime('%Y-%m'), pfx, texto.upper(), start_date.strftime('%d_%m_%Y'), com)
                                response = requests.get(url) # url com texto em uppercase
                                print(url)
                                if response.ok: # se True
                                    # print("COMPLEMENTO = ", com)
                                    # print("link do dia ", start_date.strftime("%d-%m"))
                                    # print(url)
                                    data_check = True
                                    break # quebra loop complements
            
                        if response.ok:
                            break # quebra loop pfx in prefixes

                else:
                    url = "http://www.saude.pr.gov.br/sites/default/arquivos_restritos/files/documento/2020-08/INFORME-EPIDEMIOLOGICO-12-08-2020.pdf"
                    # print(url)
                    response = requests.get(url)
                    data_check = True

            else: # 30/04 url issue -> /2020-05/informe_epidemiologico_30_04_2020_0.pdf"
                url = "http://www.saude.pr.gov.br/sites/default/arquivos_restritos/files/documento/2020-05/informe_epidemiologico_30_04_2020_0.pdf"
                # print(url)
                response = requests.get(url)
                data_check = True
        else:
            url = "https://www.saude.pr.gov.br/sites/default/arquivos_restritos/files/documento/2021-04/informe_epidemiologico_nn01_04_2021.pdf"
            # print(url)
            response = requests.get(url)
            data_check = True

        if not response.ok:
            if not data_check:
                # print("get_sesa_time_pr sem boletim")
                return
            break
        
        template_path = templateSelector(start_date)
        df = tabula.read_pdf_with_template(url, template_path, pandas_options={'header': None, 'dtype': int})

        # print(df)
        print(start_date)
        # for d in df:
        #     print(d)

        # wld = df[0]
        br = df[1]
        pr = df[2]

        print(br)
        # print(pr)

        # wld = clean_WLD(wld, start_date)
        br = clean_BR(br, start_date)
        pr = clean_PR(pr)
        # for d in df:
        #     print(d)

        print(pr)
        # print(br)

        # old version xx-x -> 12-2 
        # temp_pr = pd.DataFrame([[df[0][2][1], df[0][2][2]]], columns=['cases', 'deaths'])
        # temp_br = pd.DataFrame([[df[0][1][1], df[0][1][2]]], columns=['cases', 'deaths'])
        # temp_wld = pd.DataFrame([[df[0][0][1], df[0][0][2]]], columns=['cases', 'deaths'])
        #working 13-2 -> 31-3
       
        temp_pr = pd.DataFrame([[pr[0][1], pr[0][2]]], columns=['cases', 'deaths'])
        temp_br = pd.DataFrame([[br[0][1], br[0][2]]], columns=['cases', 'deaths'])
        # temp_wld = pd.DataFrame([[wld[0][1], wld[0][2]]], columns=['cases', 'deaths'])

        # print("WLD")
        # print(temp_wld)
        # print("BR")
        # print(temp_br)
        # print("PR")
        # print(temp_pr)
        
        # old version xx-x -> 12-2
        # temp_pr = transform(temp_pr)
        # temp_br = transform(temp_br)
        # temp_wld = transform(temp_wld)

        temp_pr['date'] = start_date
        temp_br['date'] = start_date
        # temp_wld['date'] = start_date

        final_pr = pd.concat([final_pr, temp_pr], ignore_index=True)
        final_br = pd.concat([final_br, temp_br], ignore_index=True)
        # final_wld = pd.concat([final_wld, temp_wld], ignore_index=True)

        start_date += timedelta(days=1)
  
    print("PR")
    print(final_pr)
    # print("BR")
    # print(final_br)
    # print("WLD")
    # print(final_wld)
    
    if data_check: 
        final_pr.to_sql("SESA_time_PR", index=False, con=session.get_bind(), if_exists='append', method='multi',
        dtype={
            'cases': Integer(),
            'deaths': Integer(),
            'date': Date()
        })
        # final_br.to_sql("SESA_time_Br", index=False, con=session.get_bind(), if_exists='append', method='multi',
        # dtype={
        #     'cases': Integer(),
        #     'deaths': Integer(),
        #     'date': Date()
        # })
        # final_wld.to_sql("SESA_time_mundo", index=False, con=session.get_bind(), if_exists='append', method='multi',
        # dtype={
        #     'cases': Integer(),
        #     'deaths': Integer(),
        #     'date': Date()
        # })
        # print("sesa_time_pr inserido com sucesso")
    
    # else:
    #     print("sesa_time_pr está atualizado")