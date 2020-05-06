import pandas as pd
import requests
import json

url = ('https://brasil.io/api/dataset/covid19/caso/data')
listdate = []


def getData(url):
    req = requests.get(url, timeout=3000)
    response = req.json()

    return response


def datasetBuilder(listdate):
    head = [
        'Cidade',
        'IBGE',
        'Confirmados',
        'Confirmados_100K',
        'Data',
        'Taxa_Morte',
        'Mortes',
        'Populacao',
        'Ultimo_Ref',
        'Tipo_Local',
        'Estado'
    ]

    dataset = pd.DataFrame(listdate, columns=head)

    return dataset


while url is not None:
    response = getData(url)
    result = response.get('results')
    for row in result:
        city = row.get('city')
        ibge_code = row.get('city_ibge_code')
        confirmed = row.get('confirmed')
        confirmed_100k = row.get('confirmed_per_100k_inhabitants')
        date = row.get('date')
        death_rate = row.get('death_rate')
        deaths = row.get('deaths')
        population = row.get('estimated_population_2019')
        is_last = row.get('is_last')
        place_type = row.get('place_type')
        state = row.get('state')
        listdate.append([
            city,
            ibge_code,
            confirmed,
            confirmed_100k,
            date,
            death_rate,
            deaths,
            population,
            is_last,
            place_type,
            state
        ])
    url = response.get('next')

dataset = datasetBuilder(listdate)

print(dataset)
