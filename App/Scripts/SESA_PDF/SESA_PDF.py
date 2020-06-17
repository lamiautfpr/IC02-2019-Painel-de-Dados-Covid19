from Scripts.functions import now, urlGenerator, getApi, getNextDate, formatDate
from DataBase import sqlCreator
from sqlalchemy.types import String, Date, Integer, Float
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
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
        'uti infantil tx ocup': Integer(),
        'enf infantil exist': Float(),
        'enf infantil ocup': Integer(),
        'enf infantil tx ocup': Integer()
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
    ocupacao = dfs[list_sheets[0]] # A coluna 4 tem valores de 3 colunas
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
    
   
    
    #TRATANDO DF LEITOS
    leitos = dfs[list_sheets[1]][5:].astype(str).values.tolist()
    new_leitos = [] # stack de new_line
    # print(type(leitos))
    for lei in leitos:
        new_line = [] # stack de palavras
        for ll in lei:
            #QUEBRA
            if len(ll) > 8: # MINIMO PARA QUEBRA len(0% 0 0 0%) = 9 ou > que (len("NOROESTE"))
                ll = ll.split(' ')
                for l in ll:
                    new_line.append(l) # stack 1 por 1
            else: 
                new_line.append(ll) # stack na linha toda
        new_leitos.append(new_line) # stack final pro DF

    leitos = pd.DataFrame(new_leitos) # DF Criado
    leitos.columns = leitos_columns # Columas arrumadas



    #Calculo das porcentagens LEITOS
    porcentagem = lambda x,y: ((x/y)*100)
    leitos['uti adulto tx ocup'] = porcentagem(leitos['uti adulto ocup'].str.replace(".", "").astype(int), leitos['uti adulto exist'].str.replace(".", "").astype(int))
    leitos['enf adulto tx ocup'] = porcentagem(leitos['enf adulto ocup'].str.replace(".", "").astype(int), leitos['enf adulto exist'].str.replace(".", "").astype(int))
    leitos['uti infantil tx ocup'] = porcentagem(leitos['uti infantil ocup'].str.replace(".", "").astype(int), leitos['uti infantil exist'].str.replace(".", "").astype(int))
    leitos['enf infantil tx ocup'] = porcentagem(leitos['enf infantil ocup'].str.replace(".", "").astype(int), leitos['enf infantil exist'].str.replace(".", "").astype(int))


    #TRATANDO DF CASOS
    casos = dfs[list_sheets[2]]
    casos = casos[3:].drop(columns=[2, 5])
    casos.columns = casos_columns
    
    #Calculo das porcentagens CASOS
    total_cases = casos.iloc[-1, 1].replace(".", "")
    total_obitos = casos.iloc[-1, -2].replace(".", "")
    casos['casos porcentagem'] = porcentagem(casos['casos'].str.replace(".", "").astype(int), int(total_cases))
    casos['obitos porcentagem'] = porcentagem(casos['obitos'].str.replace(".", "").astype(int), int(total_obitos))
    
    #TRATANDO DF COMORBIDADES
    comorb = dfs[list_sheets[3]][2:].astype(str).values.tolist()
    
    new_comorb = []
    for cc in comorb:
        for c in cc:
            c = c.rsplit(' ', 2) # Quebra a lista separando os ultimos 2 elementos
            new_comorb.append(c)    
    
    new_comorb = pd.DataFrame(new_comorb)
    new_comorb.columns = comorb_columns
    # print(new_comorb)

    # print(total)
    total_num = new_comorb.iloc[-1, -2]
    new_comorb['porcentagem'] = porcentagem(new_comorb['numero'].str.replace(".", "").astype(int), int(total_num))


    # reset dfs

    ocupacao.drop(columns=['sus total', 'priv total', 'total susp', 'total conf', 'total total'], inplace=True)

    dfs[list_sheets[0]] = ocupacao
    dfs[list_sheets[1]] = leitos
    dfs[list_sheets[2]] = casos
    dfs[list_sheets[3]] = new_comorb
    
    #to numeric
    dfs = transform(dfs)

    return dfs

def get_data(session):

    url = 'http://www.saude.pr.gov.br/sites/default/arquivos_restritos/files/documento/2020-06/informe_epidemiologico_16_06_2020.pdf'

    df = tabula.read_pdf(url, pages=['5', '12'], pandas_options={'header': None, 'dtype': str})

    dfs = {}
    
    i = 0
    for sheet in data_types:
        print(sheet)
        dfs[sheet] = df[i]
        i+=1

    dfs = cleanner(dfs)

    for sheet in data_types:
        dfs[sheet].to_sql('SESA_PDF_{}'.format(sheet), con=session.get_bind(), if_exists='replace', method='multi',
        dtype=data_types[sheet])
    return 'Fim Da Extracao Dos Dados'
