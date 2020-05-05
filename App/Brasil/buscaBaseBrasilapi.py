import pandas as pd
import requests
import json

url = ('https://covid19-brazil-api.now.sh/api/report/v1')
listdate = []


def getData(url):
    req = requests.get(url, timeout=3000)
    response = req.json()

    return response


def datasetBuilder(listdate):
    head = [
        'ID',
        'UF',
        'Estado',
        'Confirmados',
        'Mortes',
        'Suspeitos',
        'Descartados',
        'Data'
    ]

    dataset = pd.DataFrame(listdate, columns=head)

    return dataset


while url is not None:
    response = getData(url)
    result = response.get('data')
    for row in result:
        uid = row.get('uid')
        uf = row.get('uf')
        state = row.get('state')
        confirmed = row.get('cases')
        deaths = row.get('deaths')
        suspects = row.get('suspects')
        refuses = row.get('refuses')
        date = row.get('datetime')

        listdate.append([
            uid,
            uf,
            state,
            confirmed,
            deaths,
            suspects,
            refuses,
            date
        ])
    url = response.get('next')

dataset = datasetBuilder(listdate)

print(dataset)
