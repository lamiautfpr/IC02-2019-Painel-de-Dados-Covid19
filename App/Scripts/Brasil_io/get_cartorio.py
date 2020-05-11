from Scripts.functions import urlGeneretor
from DataBase import sqlCreator
import json


def insertData(session):
    insertObj = sqlCreator.Insert(session)
    selectObj = sqlCreator.Select(session)

    date = selectObj.LastDate("date", "Brasil_io_base_cartorio")
    url = getData(urlGeneretor(2, date))

    while url is not None:
        listdate = []
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
            insertObj.Brasilio_cartorio(listdate)

        url = response.get('next')

    return ''
