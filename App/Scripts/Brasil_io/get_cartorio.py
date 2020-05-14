from Scripts.functions import urlGenerator, getApi
from DataBase import sqlCreator

def insertData(session):
    insertObj = sqlCreator.Insert(session)
    selectObj = sqlCreator.Select(session)
    listdate = []
    loop = True

    # date = selectObj.LastDate("date", "Brasil_io_base_cartorio")
    date = "01-01-2020"
    url = urlGeneretor(2, date)
    res = getApi(url)

    while url is not None:
        next = res.get("next")
        result = res.get('results')

        for row in result:
            date = row.get('date')
            state = row.get('state')
            epidemiological_week_2019 = row.get('epidemiological_week_2019')
            epidemiological_week_2020 = row.get('epidemiological_week_2020')
            deaths_total_2019 = row.get('deaths_total_2019')
            deaths_total_2020 = row.get('deaths_total_2020')
            new_deaths_total_2019 = row.get('new_deaths_total_2019')
            deaths_covid19 = row.get('deaths_covid19')
            new_deaths_total_2020 = row.get('new_deaths_total_2020')
            deaths_indeterminate_2019 = row.get('deaths_indeterminate_2019')
            deaths_indeterminate_2020 = row.get('deaths_indeterminate_2020')
            deaths_others_2019 = row.get('deaths_others_2019')
            deaths_others_2020 = row.get('deaths_others_2020')
            deaths_pneumonia_2019 = row.get('deaths_pneumonia_2019')
            deaths_pneumonia_2020 = row.get('deaths_pneumonia_2020')
            deaths_respiratory_failure_2019 = row.get('deaths_respiratory_failure_2019')
            deaths_respiratory_failure_2020 = row.get('deaths_respiratory_failure_2020')
            deaths_sars_2019 = row.get('deaths_sars_2019')
            deaths_sars_2020 = row.get('deaths_sars_2020')
            deaths_septicemia_2019 = row.get('deaths_septicemia_2019')
            deaths_septicemia_2020 = row.get('deaths_septicemia_2020')
            new_deaths_covid19 = row.get('new_deaths_covid19')
            new_deaths_indeterminate_2019 = row.get('new_deaths_indeterminate_2019')
            new_deaths_indeterminate_2020 = row.get('new_deaths_indeterminate_2020')
            new_deaths_others_2019 = row.get('new_deaths_others_2019')
            new_deaths_others_2020 = row.get('new_deaths_others_2020')
            new_deaths_pneumonia_2019 = row.get('new_deaths_pneumonia_2019')
            new_deaths_pneumonia_2020 = row.get('new_deaths_pneumonia_2020')
            new_deaths_respiratory_failure_2019 = row.get('new_deaths_respiratory_failure_2019')
            new_deaths_respiratory_failure_2020 = row.get('new_deaths_respiratory_failure_2020')
            new_deaths_sars_2019 = row.get('new_deaths_sars_2019')
            new_deaths_sars_2020 = row.get('new_deaths_sars_2020')
            new_deaths_septicemia_2019 = row.get('new_deaths_septicemia_2019')
            new_deaths_septicemia_2020 = row.get('new_deaths_septicemia_2020')

            listdate = [
                date,
                state,
                epidemiological_week_2019,
                epidemiological_week_2020,
                deaths_total_2019,
                deaths_total_2020,
                new_deaths_total_2019,
                deaths_covid19,
                new_deaths_total_2020,
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
                new_deaths_septicemia_2020
            ]

            insertObj.Brasilio_cartorio(listdate)

        if next is None:
            loop = False
        else:
            res = getApi(next)

    return ''
