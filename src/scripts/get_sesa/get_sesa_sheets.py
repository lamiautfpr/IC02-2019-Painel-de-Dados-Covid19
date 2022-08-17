import requests
import pandas as pd
from scripts.functions import now, format_date, previous_date


def catcher():
    gid = [
        '312396411', '1684210468', '1984868632', '816983062',
        '1368715649', '594742355', '1483238027', '1301182333'
    ]
    datasets = []

    date = now().date()

    # r = requests.get('http://www.saude.pr.gov.br/sites/default/'
    #                 'arquivos_restritos/files/documento/2020-0{}/INFORME_EPIDEMIOLOGICO_{}.pdf'
    #                 .format(date.month, format_date(0, date)))
    # r.raise_for_status

    # while not r.ok:
    #     date = previous_date(date)

    #     r = requests.get('http://www.saude.pr.gov.br/sites/default/'
    #                     'arquivos_restritos/files/documento/2020-0{}/INFORME_EPIDEMIOLOGICO_{}.pdf'
    #                     .format(date.month, format_date(0, date)))
    #     r.raise_for_status

    for gids in gid:
        url = "https://docs.google.com/spreadsheets/d/1I2F3PRBv_9Al1rDSWH9eClHvWZ49op9AQFWqgNjkj70/export?gid={}&format=csv".format(gids)
        # url = ("https://docs.google.com/spreadsheets/d/1mw17ZXJaRML5QKcZPACVE-"
        #        "j7gJoqyv-TnOyG5ZCKINM/export?gid={}&format=csv".format(gids))
        dataset = pd.read_csv(url, encoding='utf-8',
                              engine='python', error_bad_lines=False)
        dataset.insert(len(dataset.columns), "insert_date", now())
        dataset.insert(len(dataset.columns), "data_boletim", date)
        datasets.append(dataset)
    return datasets


def insert(session):
    print("Inserindo get_sesa_sheets.")

    datasets = catcher()
    titles = [
        'dadosGerais', 'faixaEtaria', 'evoluConfirmados', 'vacinas',
        'examesRT', 'casosSRAG', 'comorbidadesObitos', 'obitosCor'
    ]
    for idx, title in enumerate(titles):
        datasets[idx].to_sql('SESA_base_{}'.format(title), con=session.get_bind(), 
                                    index_label='id', if_exists='replace', method='multi', chunksize=50000)
    return print("sesa_sheets inserido com sucesso!")
