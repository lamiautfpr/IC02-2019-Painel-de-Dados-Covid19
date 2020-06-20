from Scripts.functions import now, urlGenerator, getApi, getPreviousDate, formatDate
from datetime import datetime
from DataBase import tableClass
import pandas as pd
import requests

def catcher():
    gid = ['1593460334', '618041857', '1431072159', '1317012264', '1222957039', '1297484146', '354728218', '355601818', '1342035615']

    listDatasets = []

    date = datetime.now().date()

    r = requests.get('http://www.saude.pr.gov.br/sites/default/arquivos_restritos/files/documento/2020-0{}/INFORME_EPIDEMIOLOGICO_{}.pdf'.format(date.month, formatDate(4, date)))
    r.raise_for_status

    while not r.ok:
        date = getPreviousDate(date)

        r = requests.get('http://www.saude.pr.gov.br/sites/default/arquivos_restritos/files/documento/2020-0{}/INFORME_EPIDEMIOLOGICO_{}.pdf'.format(date.month, formatDate(4, date)))
        r.raise_for_status
    
    i = 0
    while i < len(gid):
        url = ("https://docs.google.com/spreadsheets/d/1mw17ZXJaRML5QKcZPACVE-j7gJoqyv-TnOyG5ZCKINM/export?gid={}&format=csv".format(gid[i]))
        dataset = pd.read_csv(url, encoding='utf-8', engine='python', error_bad_lines=False)
        
        dataset.insert(len(dataset.columns), "data_boletim", date)
        dataset.insert(len(dataset.columns), "insert_date", now())

        listDatasets.append(dataset)
        
        i += 1
    return listDatasets

def insertData(session):
    print("Coletando e inserindo dados para SESA-base-PDF...")

    listDatasets = catcher()
    listTitles = ['dadosGerais', 'faixaEtaria', 'evoluConfirmados', 'examesRT', 'ocupacaoLeitos', 'leitosMacrorregiao', 'casosSRAG', 'comorbidadesObitos', 'obitosCor']

    i = 0
    while i < len(listDatasets):
        listDatasets[i].to_sql('SESA_base_{}'.format(listTitles[i]), con=session.get_bind(), index_label='id', if_exists='replace', method='multi', chunksize=50000)
        i += 1
    return