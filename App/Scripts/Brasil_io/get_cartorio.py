from Scripts.functions import getData, urlGenerator
from DataBase import sqlCreator
import json
from datetime import datetime


def insertData(session):
    insertObj = sqlCreator.Insert(session)
    selectObj = sqlCreator.Select(session)

    last_date = selectObj.LastDate("date", "Brasil_io_base_cartorio")
    url = urlGenerator(2)
    response = getData(url)
    updated = False

    while url is not None and not updated:
        listdate = []
        result = response.get('results')
        for row in result:
            date = row.get('date')
            if last_date is None:
                pass
            elif datetime.strptime(date, '%Y-%m-%d').date() <= last_date:
                updated = True
                break
            deaths_covid19 = row.get('deaths_covid19')
            deaths_indeterminate_2019 = row.get('deaths_indeterminate_2019')
            deaths_indeterminate_2020 = row.get('deaths_indeterminate_2020')
            deaths_others_2019 = row.get('deaths_others_2019')
            deaths_others_2020 = row.get('deaths_others_2020')
            deaths_pneumonia_2019 = row.get('deaths_pneumonia_2019')
            deaths_pneumonia_2020 = row.get('deaths_pneumonia_2020')
            deaths_respiratory_failure_2019 = row.get(
                'deaths_respiratory_failure_2019')
            deaths_respiratory_failure_2020 = row.get(
                'deaths_respiratory_failure_2020')
            deaths_sars_2019 = row.get('deaths_sars_2019')
            deaths_sars_2020 = row.get('deaths_sars_2020')
            deaths_septicemia_2019 = row.get('deaths_septicemia_2019')
            deaths_septicemia_2020 = row.get('deaths_septicemia_2020')
            deaths_total_2019 = row.get('deaths_total_2019')
            deaths_total_2020 = row.get('deaths_total_2020')
            epidemiological_week_2019 = row.get('epidemiological_week_2019')
            epidemiological_week_2020 = row.get('epidemiological_week_2020')
            new_deaths_covid19 = row.get('new_deaths_covid19')
            new_deaths_indeterminate_2019 = row.get(
                'new_deaths_indeterminate_2019')
            new_deaths_indeterminate_2020 = row.get(
                'new_deaths_indeterminate_2020')
            new_deaths_others_2019 = row.get('new_deaths_others_2019')
            new_deaths_others_2020 = row.get('new_deaths_others_2020')
            new_deaths_pneumonia_2019 = row.get('new_deaths_pneumonia_2019')
            new_deaths_pneumonia_2020 = row.get('new_deaths_pneumonia_2020')
            new_deaths_respiratory_failure_2019 = row.get(
                'new_deaths_respiratory_failure_2019')
            new_deaths_respiratory_failure_2020 = row.get(
                'new_deaths_respiratory_failure_2020')
            new_deaths_sars_2019 = row.get('new_deaths_sars_2019')
            new_deaths_sars_2020 = row.get('new_deaths_sars_2020')
            new_deaths_septicemia_2019 = row.get('new_deaths_septicemia_2019')
            new_deaths_septicemia_2020 = row.get('new_deaths_septicemia_2020')
            new_deaths_total_2019 = row.get('new_deaths_total_2019')
            new_deaths_total_2020 = row.get('new_deaths_total_2020')
            state = row.get('state')
            listdate = [
                date,
                deaths_covid19,
                deaths_indeterminate_2019,
                deaths_indeterminate_2020,
                deaths_others_2019,
                deaths_others_2020,
                deaths_pneumonia_2019,
                deaths_pneumonia_2020,
                deaths_respiratory_failure_2019,
                deaths_respiratory_failure_2020,
                deaths_sars_2019,
                deaths_sars_2020,
                deaths_septicemia_2019,
                deaths_septicemia_2020,
                deaths_total_2019,
                deaths_total_2020,
                epidemiological_week_2019,
                epidemiological_week_2020,
                new_deaths_covid19,
                new_deaths_indeterminate_2019,
                new_deaths_indeterminate_2020,
                new_deaths_others_2019,
                new_deaths_others_2020,
                new_deaths_pneumonia_2019,
                new_deaths_pneumonia_2020,
                new_deaths_respiratory_failure_2019,
                new_deaths_respiratory_failure_2020,
                new_deaths_sars_2019,
                new_deaths_sars_2020,
                new_deaths_septicemia_2019,
                new_deaths_septicemia_2020,
                new_deaths_total_2019,
                new_deaths_total_2020,
                state,
            ]
            insertObj.Brasilio_cartorio(listdate)

        if not updated:
            url = response.get('next')
            if url:
                response = getData(url)

    return ''
