from Scripts.functions import now, urlGenerator, getApi, getNextDate, formatDate
from DataBase import sqlCreator
from sqlalchemy.types import String, Date, Integer, Float
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import requests
import tabula

list_sheets = [
    'ocupacaoLeitos', #PG 5
    'leitosMacrorregiao', #PG 5
    'casosSRAG',  #PG 12-1
    'comorbidadesObitos' #PG 12-2
]

data_types = {
    'ocupacaoLeitos':{
        'tipo de leito': String(),
        'sus susp': Integer(),
        'sus conf': Integer(),
        'priv susp': Integer(),
        'priv conf': Integer()
    },
    'leitosMacrorregiao':{
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
        'enf infantil tx ocup': Float()
    },
    'casosSRAG':{
        'srag': String(),
        'casos': Integer(),
        'casos porcentagem': Float(),
        'obitos': Integer(),
        'obitos porcentagem': Float()
    },
    'comorbidadesObitos':{
        'comorbidade obitos': String(),
        'numero': Integer(),
        'porcentagem': Float()
    }
}

ocupacao_columns = [
    'tipo de leito',
    'sus susp',
    'sus conf',
    'sus total',
    'priv susp',
    'priv conf',
    'priv total',
    'total susp',
    'total conf',
    'total total'
]

casos_columns = [
    'srag',
    'casos',
    'casos porcentagem',
    'obitos',
    'obitos porcentagem'
]

comorb_columns = [
    'comorbidade obitos',
    'numero',
    'porcentagem'
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

    for sheet in list_sheets:
        for df in dfs[sheet]:
            try:
                dfs[sheet][df] = dfs[sheet][df].str.replace(".", "").astype(int)
            except:
                pass 
        
    return dfs
        
def cleanner(dfs):

    # Tratando ocupacoes
    ocupacao = dfs[list_sheets[0]]
    ocupacao = pd.concat([ocupacao[4:6], ocupacao[7:8]]).astype(str).values.tolist()
    new_ocupacao = [] # stack de new lines
    
    for ocup in ocupacao:
        new_line = [] # stack line
        for oo in ocup:
            if len(oo) > 5:
                oo = oo.split(' ')
                for o in oo:
                    new_line.append(o)
            else:
                new_line.append(oo)
        new_ocupacao.append(new_line)

    ocupacao = pd.DataFrame(new_ocupacao)
    ocupacao.columns = ocupacao_columns
    ocupacao.iloc[-1][0] = "UTI E CLINICO"
    ocupacao.drop(columns=['sus total', 'priv total', 'total susp', 'total conf', 'total total'], inplace=True)

    
    #TRATANDO DF LEITOS
    leitos = dfs[list_sheets[1]].dropna().astype(str).values.tolist()
    new_leitos = []
    # print(type(leitos))
    for lei in leitos:
        new_line = [] 
        for ll in lei:
            #QUEBRA
            if len(ll) > 8: # MINIMO PARA QUEBRA len(0% 0 0 0%) = 9 ou > que (len("NOROESTE"))
                ll = ll.split(' ')
                for l in ll:
                    new_line.append(l) 
            else: 
                new_line.append(ll) 
        new_leitos.append(new_line) 

    leitos = pd.DataFrame(new_leitos) 
    leitos.columns = leitos_columns 

    porcentagem = lambda x,y: ((x/y)*100)
    leitos['uti adulto tx ocup'] = porcentagem(leitos['uti adulto ocup'].str.replace(".", "").astype(int), leitos['uti adulto exist'].str.replace(".", "").astype(int))
    leitos['enf adulto tx ocup'] = porcentagem(leitos['enf adulto ocup'].str.replace(".", "").astype(int), leitos['enf adulto exist'].str.replace(".", "").astype(int))
    leitos['uti infantil tx ocup'] = porcentagem(leitos['uti infantil ocup'].str.replace(".", "").astype(int), leitos['uti infantil exist'].str.replace(".", "").astype(int))
    leitos['enf infantil tx ocup'] = porcentagem(leitos['enf infantil ocup'].str.replace(".", "").astype(int), leitos['enf infantil exist'].str.replace(".", "").astype(int))

    #TRATANDO DF CASOS
    casos = dfs[list_sheets[2]]
    if len(casos) == 6:
        casos = casos[3:].drop(columns=[2, 5])
    else: #len = 4
        casos.dropna(inplace=True)

    casos.columns = casos_columns

    total_cases = casos.iloc[-1, 1].replace(".", "")
    total_obitos = casos.iloc[-1, -2].replace(".", "")
    casos['casos porcentagem'] = porcentagem(casos['casos'].str.replace(".", "").astype(int), int(total_cases))
    casos['obitos porcentagem'] = porcentagem(casos['obitos'].str.replace(".", "").astype(int), int(total_obitos))
    
    
    #TRATANDO DF COMORBIDADES
    comorb = dfs[list_sheets[3]][2:].astype(str).values.tolist()
    print(comorb)
    
    new_comorb = []
    if len(comorb) == 1:
        for cc in comorb:
            for c in cc:
                c = c.rsplit(' ', 2)
                new_comorb.append(c)    
                new_comorb = pd.DataFrame(new_comorb)
    else:# len = 3
        new_comorb = pd.DataFrame(comorb)

   
    new_comorb.columns = comorb_columns

    # print(total)
    total_num = new_comorb.iloc[-1, -2]
    new_comorb['porcentagem'] = porcentagem(new_comorb['numero'].str.replace(".", "").astype(int), int(total_num))

    # reset dfs
    dfs[list_sheets[0]] = ocupacao
    dfs[list_sheets[1]] = leitos
    dfs[list_sheets[2]] = casos
    dfs[list_sheets[3]] = new_comorb
    
    dfs = transform(dfs)

    return dfs

def get_data(session):

    texto = 'informe_epidemiologico'
    base_url = 'http://www.saude.pr.gov.br/sites/default/arquivos_restritos/files/documento/{}/{}_{}.pdf'

    hoje = now()
    # hoje = datetime(2020, 6, 17, 19, 0, 0)
    url = base_url.format(hoje.strftime('%Y-%m'), texto, hoje.strftime('%d_%m_%Y'))
    response = requests.get(url)
    
    df = pd.DataFrame()

    if not response.ok:
        url = base_url.format(hoje.strftime('%Y-%m'), texto.upper(), hoje.strftime('%d_%m_%Y'))
        response = requests.get(url)

    if not response.ok:
        print("erro link")
    else:

        df = tabula.read_pdf(url, pages=['5', '12'], pandas_options={'header': None, 'dtype': str})

        dfs = {}
        i = 0
        for d in df:
            if len(d) >= 9:
                dfs[list_sheets[i]] = d
                print(d)
                i+=1

        # with pd.ExcelWriter('SESA_{}.xlsx'.format(hoje.strftime('%d'))) as writer:
        #     for sheet in data_types:
        #         dfs[sheet].to_excel(writer, index=False, engine='xlsxwriter', encoding=' UTF-8', sheet_name='SESA_{}'.format(sheet))
       
        dfs = cleanner(dfs)

        # with pd.ExcelWriter('SESA_{}-Clean.xlsx'.format(hoje.strftime('%d'))) as writer:
        #     for sheet in data_types:
        #         print("Inserindo ", sheet, "no documento")
        #         dfs[sheet].to_excel(writer, index=False, engine='xlsxwriter', encoding=' UTF-8', sheet_name='SESA_TIME_{}'.format(sheet))

        for sheet in data_types:
            dfs[sheet].to_sql('SESA_PDF_{}'.format(sheet), con=session.get_bind(), if_exists='replace', method='multi',
            dtype=data_types[sheet])

    return 'Fim Da Extracao Dos Dados'
