from scripts.functions import now
from database import sql_creator
from sqlalchemy.types import String, Date, Integer, Float, DateTime
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import requests
import tabula


ocupacao_columns = [
    'tipo_de_leito',
    'sus_suspeitos',
    'sus_confirmados',
    'sus total',
    'particular_suspeitos',
    'particular_confirmados',
    'priv total',
    'total susp',
    'total conf',
    'total total'
]

leitos_columns = [
    'leitos',
    'uti adulto exist',
    'uti adulto ocup',
    'uti adulto tx ocup',
    'enf adulto exist',
    'enf adulto ocup',
    'enf adulto tx ocup',
    'uti infantil exist',
    'uti infantil ocup',
    'uti infantil tx ocup',
    'enf infantil exist',
    'enf infantil ocup',
    'enf infantil tx ocup'
]


def transform(dfs):

    for df in dfs:
        for d in df:
            try:              
                df[d] = df[d].str.replace(".", "").str.replace("%", "").astype(int)
            except:
                pass
    return dfs  

def cleanner(dfs):

    if len(dfs) == 2:
    
        ocupacao = dfs[0]
        ocupacao.dropna(thresh=3, axis='columns', inplace=True) # Dropa coluna com menos de 3 valones não nulos

        if len(ocupacao.dropna()) == 3: # start 24-6
            print("DropNa = 3")
            if(len(ocupacao)) <=6:
                print("Tamanho <= 6") # 24-6 -> 15-7
                ocupacao.dropna(inplace=True)
                ocupacao[0] = ''
                ocupacao = ocupacao.astype(str).values.tolist()
                
            else: # 16-7 -> ??-??
                print('Tamanho > 6')
                ocupacao.dropna(thresh=2, inplace=True)
                ocupacao = ocupacao[2:].astype(str).values.tolist()

        else: # 10-6 -> 23-6 / 17-7
            print("DropNa != 3")
            if(len(ocupacao) < 8 ): # 17-7 -> 18-7
                print("ENTROU AQUI")
                ocupacao[0] = ''
                ocupacao = ocupacao[2:].astype(str).values.tolist()
            else: # 10-6 -> 23-6
                ocupacao.dropna(thresh=2, inplace=True)
                ocupacao = ocupacao[2:].astype(str).values.tolist()
            
        new_ocupacao = []
        for ocup in ocupacao:
            new_line = []
            for oo in ocup:
                if len(oo) > 5:
                    oo = oo.split(' ')
                    for o in oo:
                        new_line.append(o)
                else:
                    new_line.append(oo)
            new_ocupacao.append(new_line)

        ocupacao = pd.DataFrame(new_ocupacao)
        ocupacao.iloc[0][0] = "UTI"
        ocupacao.iloc[1][0] = "CLÍNICO"
        ocupacao.iloc[-1][0] = "UTI E CLÍNICO"

        # print('======================================')
        # print(ocupacao)
        # print('======================================')
        ocupacao.columns = ocupacao_columns
        ocupacao.drop(columns=['sus total', 'priv total', 'total susp', 'total conf', 'total total'], inplace=True)
        
        leitos = dfs[1].dropna().astype(str).values.tolist() 
        new_leitos = []
        for lei in leitos:
            new_line = [] 
            for ll in lei:
                if len(ll.split(' ')) > 1:
                    ll = ll.split(' ')
                    for l in ll:
                        new_line.append(l) 
                else: 
                    new_line.append(ll) 
            new_leitos.append(new_line) 

        leitos = pd.DataFrame(new_leitos)

        #24-6 -> ??-?
        if len(leitos.columns) == 17:
            leitos.drop(columns=[4, 8, 12, 16], inplace=True)
        elif len(leitos.columns) == 16:
            leitos.insert(0, 'asda', ['LESTE', 'OESTE', 'NOROESTE', 'NORTE', 'TOTAL']) # pos, name, [values]
            leitos.drop(columns=[2, 6, 10, 14], inplace=True)

        leitos.columns = leitos_columns 
        porcentagem = lambda x,y: ((x/y)*100)
        leitos['uti adulto tx ocup'] = porcentagem(leitos['uti adulto ocup'].str.replace(".", "").astype(int), leitos['uti adulto exist'].str.replace(".", "").astype(int))
        leitos['enf adulto tx ocup'] = porcentagem(leitos['enf adulto ocup'].str.replace(".", "").astype(int), leitos['enf adulto exist'].str.replace(".", "").astype(int))
        leitos['uti infantil tx ocup'] = porcentagem(leitos['uti infantil ocup'].str.replace(".", "").astype(int), leitos['uti infantil exist'].str.replace(".", "").astype(int))
        leitos['enf infantil tx ocup'] = porcentagem(leitos['enf infantil ocup'].str.replace(".", "").astype(int), leitos['enf infantil exist'].str.replace(".", "").astype(int))

        dfs[0] = ocupacao
        dfs[1] = leitos

    else:
        leitos = dfs[0].dropna().astype(str).values.tolist()
        new_leitos = []

        for lei in leitos:
            new_line = [] 
            for ll in lei:
                if len(ll.split(' ')) > 1:
                    ll = ll.split(' ')
                    for l in ll:
                        new_line.append(l) 
                else: 
                    new_line.append(ll) 
            new_leitos.append(new_line) 

        leitos = pd.DataFrame(new_leitos) 
        leitos.columns = leitos_columns 
        porcentagem = lambda x,y: ((x/y)*100)
        leitos['uti adulto tx ocup'] = porcentagem(leitos['uti adulto ocup'].str.replace(".", "").str.replace("%", "").astype(int), leitos['uti adulto exist'].str.replace(".", "").str.replace("%", "").astype(int))
        leitos['enf adulto tx ocup'] = porcentagem(leitos['enf adulto ocup'].str.replace(".", "").str.replace("%", "").astype(int), leitos['enf adulto exist'].str.replace(".", "").str.replace("%", "").astype(int))
        leitos['uti infantil tx ocup'] = porcentagem(leitos['uti infantil ocup'].str.replace(".", "").str.replace("%", "").astype(int), leitos['uti infantil exist'].str.replace(".", "").str.replace("%", "").astype(int))
        leitos['enf infantil tx ocup'] = porcentagem(leitos['enf infantil ocup'].str.replace(".", "").str.replace("%", "").astype(int), leitos['enf infantil exist'].str.replace(".", "").str.replace("%", "").astype(int))

        dfs[0] = leitos
        
    dfs = transform(dfs)
    return dfs

def insert(session):
    
    print("Inserindo get_sesa_leitos.")

    data_check = False
    complements = ['_atualizado', '_1', '_0', '']
    texto = 'informe_epidemiologico'
    base_url = 'http://www.saude.pr.gov.br/sites/default/arquivos_restritos/files/documento/{}/{}_{}{}.pdf'
    
    selectObj = sql_creator.Select(session)
    start_date = selectObj.Date('data_boletim', '"SESA_time_leitosExclusivos"') # DATABASE DATE
    start_date += timedelta(days=1)
    hoje = now().date() # HOJE 

    # TEST DATE
    # start_date = datetime(2020, 7, 17, 14, 0, 0).date()
    # hoje = datetime(2020, 7, 17, 14, 0, 0).date()

    ocupacaoLeitos = pd.DataFrame()
    leitosExclusivos = pd.DataFrame()

    while start_date <= hoje:
        for com in complements:
            url = base_url.format(start_date.strftime('%Y-%m'), texto, start_date.strftime('%d_%m_%Y'), com)
            response = requests.get(url)
            if response.ok:
                print("COMPLEMENTO = ", com)
                print("link do dia ", start_date.strftime("%d-%m"))
                print(url)
                data_check = True
                break
            else:
                url =  url = base_url.format(start_date.strftime('%Y-%m'), texto.upper(), start_date.strftime('%d_%m_%Y'), com)
                response = requests.get(url)
                if response.ok:
                    print("COMPLEMENTO = ", com)
                    print("link do dia ", start_date.strftime("%d-%m"))
                    print(url)
                    data_check = True
                    break

        if not response.ok:
            if not data_check:
                print("get_sesa_leitos is up to date")
                return
            break
        
        page = 6 if start_date >= datetime(2020, 7, 14, 14, 0, 0).date() else 5 if start_date > datetime(2020, 5, 18, 14, 0, 0).date() else 4
        print(page)
       
        df = tabula.read_pdf(url, pages=[page], pandas_options={'header': None, 'dtype': str})
         
        dfs = []
        for d in df:
            if len(d) >= 5:
                dfs.append(d)

        # for df in dfs:
        #     print(df)
        
        dfs = cleanner(dfs)
        
        for df in dfs:
            print(df)
        
        if len(dfs) == 2:
            dfs[0]['data_boletim'] = start_date
            dfs[1]['data_boletim'] = start_date
            ocupacaoLeitos = pd.concat([ocupacaoLeitos, dfs[0]])
            leitosExclusivos = pd.concat([leitosExclusivos, dfs[1]])
        else:
            dfs[0]['data_boletim'] = start_date
            leitosExclusivos = pd.concat([leitosExclusivos, dfs[0]])
        
        start_date += timedelta(days=1)

    if data_check:

        # TIME TABLES
        ocupacaoLeitos.to_sql("SESA_time_ocupacaoLeitos", con=session.get_bind(), if_exists='append', method='multi',
        dtype={
            'tipo_de_leito': String(),
            'sus_suspeitos': Integer(),
            'sus_confirmados': Integer(),
            'particular_suspeitos': Integer(),
            'particular_confirmados': Integer(),
            'data_boletim': Date()
        })

        leitosExclusivos.to_sql("SESA_time_leitosExclusivos", con=session.get_bind(), if_exists='append', method='multi',
        dtype={
            'leitos': String(),
            'uti adulto exist': Integer(),
            'uti adulto ocup': Integer(),
            'uti adulto tx ocup': Float(),
            'enf adulto exist': Integer(),
            'enf adulto ocup': Integer(),
            'enf adulto tx ocup': Float(),
            'uti infantil exist': Integer(),
            'uti infantil ocup': Integer(),
            'uti infantil tx ocup': Float(),
            'enf infantil exist': Float(),
            'enf infantil ocup': Integer(),
            'enf infantil tx ocup': Float(),
            'data_boletim': Date()
        })

        # STATIC TABLES
        dfs[0]['insert_date'] = now()
        dfs[0].to_sql("SESA_base_ocupacaoLeitos", index_label='id', con=session.get_bind(), if_exists='replace', method='multi',
        dtype={
            'tipo_de_leito': String(),
            'sus_suspeitos': Integer(),
            'sus_confirmados': Integer(),
            'particular_suspeitos': Integer(),
            'particular_confirmados': Integer(),
            'data_boletim': Date(),
            'insert_date': DateTime()
        })

        dfs[1]['insert_date'] = now()
        dfs[1].to_sql("SESA_base_leitosMacrorregiao", index_label='id', con=session.get_bind(), if_exists='replace', method='multi',
        dtype={
            'leitos': String(),
            'uti adulto exist': Integer(),
            'uti adulto ocup': Integer(),
            'uti adulto tx ocup': Float(),
            'enf adulto exist': Integer(),
            'enf adulto ocup': Integer(),
            'enf adulto tx ocup': Float(),
            'uti infantil exist': Integer(),
            'uti infantil ocup': Integer(),
            'uti infantil tx ocup': Float(),
            'enf infantil exist': Float(),
            'enf infantil ocup': Integer(),
            'enf infantil tx ocup': Float(),
            'data_boletim': Date(),
            'insert_date': DateTime()
        })
        print("sesa_leitos inserido com sucesso!")
