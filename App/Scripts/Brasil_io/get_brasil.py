from App.config.configFile import urlGeneretor
from App.DataBase import sqlCreator
import requests
import json


def getData(url):
    req = requests.get(url, timeout=3000)
    response = req.json()

    return response


def insertData(session):
    insertObj = sqlCreator.Insert(session)
    selectObj = sqlCreator.Select(session)

    date = selectObj.LastDate("date", "Brasil_io_base_nacional")

    listdate = []
    url = getData(urlGeneretor(1, date))

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
            listdate = [
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
            ]
            insertObj.Brasilio_nacional(listdate)

        url = response.get('next')

    return ''
