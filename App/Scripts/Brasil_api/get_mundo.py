import pandas as pd
import requests
import json

url = ('https://covid19-brazil-api.now.sh/api/report/v1/countries')
listdate = []

def getData(url):
    req = requests.get(url, timeout=3000)
    response = req.json()

    return response

def datasetBuilder(listdate):
    head = [
        'País',
        'Casos',
        'Confirmados',
        'Mortes',
        'Recuperados',
        'Data'
    ]

    dataset = pd.DataFrame(listdate, columns=head)

    return dataset

while url is not None:
    response = getData(url)
    result = response.get('data')
    for row in result:
        country = row.get('country')
        cases = row.get('cases')
        confirmed = row.get('confirmed')
        deaths = row.get('deaths')
        recovered = row.get('recovered')
        date = row.get('updated_at')
        listdate.append([
            country,
            cases,
            confirmed,
            deaths,
            recovered,
            date
        ])
    
    url = response.get('next')

dataset = datasetBuilder(listdate)