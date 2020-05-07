import requests
import json

url = ('https://brasil.io/api/dataset/covid19/obito_cartorio/data')
listdate = []


def getData(url):
    req = requests.get(url, timeout=3000)
    response = req.json()

    return response


while url is not None:
    response = getData(url)
    result = response.get('results')
    for row in result:
        date = row.get('date')
        deaths_covid19 = row.get('deaths_covid19')
        deaths_pneumo_2019 = row.get('new_deaths_pneumonia_2019')
        deaths_pneumo_2020 = row.get('new_deaths_pneumonia_2020')
        deaths_failure_2019 = row.get('new_deaths_respiratory_failure_2019')
        deaths_failure_2020 = row.get('new_deaths_respiratory_failure_2020')
        epidemiological_week = row.get('epidemiological_week_2020')
        new_deaths_covid19 = row.get('new_deaths_covid19')
        state = row.get('state')
        listdate = [
            date,
            deaths_covid19,
            deaths_pneumo_2019,
            deaths_pneumo_2020,
            deaths_failure_2019,
            deaths_failure_2020,
            epidemiological_week,
            new_deaths_covid19,
            state
        ]
    url = response.get('next')
