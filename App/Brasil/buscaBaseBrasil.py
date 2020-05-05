import requests
import pandas as pd
import json

brapi = ('https://covid19-brazil-api.now.sh/api/report/v1')
brio = ('https://brasil.io/api/dataset/covid19/caso/data')
listdate = []

def getData(url):        
    req = requests.get(url, timeout=3000)
    response = req.json()

    return response

def datasetBuilder(listdate):
    
    head = [
        'uf',
        'state',
        'cases',
        'deaths',
        'suspects',
        'datetime'
    ]

    dataset = pd.DataFrame(listdate, columns=head)
    
    return dataset

while brapi is not None:
    dataApi = getData(brapi)
    result = dataApi.get('data')
    for row in result:
        uf = row.get('uf')
        state = row.get('state')
        cases = row.get('cases')
        deaths = row.get('deaths')
        suspects = row.get('suspects')
        date = row.get('datetime')

        listdate.append([
            uf,
            state,
            cases,
            deaths,
            suspects,
            date
        ])
        
    brapi = dataApi.get('next')

dataset1 = datasetBuilder(listdate)

while brio is not None:
    dataIo = getData(brio)
    result = dataIo.get('results')
    for row in result:
        uf = row.get('state')
        state = row.get('city')
        cases = row.get('confirmed')
        deaths = row.get('deaths')
        suspects = (row.get('confirmed') - row.get('deaths'))
        date = row.get('date')

        listdate.append([
            uf,
            state,
            cases,
            deaths,
            suspects,
            date
        ])

    brio = dataIo.get('next')

dataset2 = datasetBuilder(listdate)

dataset = pd.concat([dataset1, dataset2])
print(dataset)