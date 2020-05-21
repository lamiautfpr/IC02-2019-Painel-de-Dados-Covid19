import pandas as pd
import requests
import json

url = ('https://covid19-brazil-api.now.sh/api/report/v1')
listdate = []

def getData(url):
    req = requests.get(url, timeout=3000)
    response = req.json()

    return response     #json com os dados da url




def datasetBuilder(listdate):
    head = [
        # 'ID',
        # 'UF'
        'Estado',
        'Confirmados',
        'Mortes',
        'Suspeitos',
        'Descartados',
        'Data'
    ]

    dataset = pd.DataFrame(listdate, columns=head)

    return dataset


# while url is not None:
response = getData(url)
result = response.get('data')
for row in result:
    # cod = row.get('ID')
    # uid = row.get('UF')
    state = row.get('state')
    cases = row.get('cases')
    deaths = row.get('deaths')
    suspects = row.get('suspects')
    refuses = row.get('refuses')
    date = row.get('datetime')
    listdate.append([
        # cod,
        # uid,
        state,
        cases,
        deaths,
        suspects,
        refuses,
        date
    ])
# url = response.get('next')

dataset = datasetBuilder(listdate)

print(dataset)
