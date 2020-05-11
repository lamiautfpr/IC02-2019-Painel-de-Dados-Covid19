from Scripts.functions import urlGeneretor, getApi
from DataBase import sqlCreator


def insertData(session):
    insertObj = sqlCreator.Insert(session)
    selectObj = sqlCreator.Select(session)
    listdate = []
    loop = True

    # date = selectObj.LastDate("date", "Brasil_io_base_nacional")
    date = "01-01-2020"
    url = urlGeneretor(1, date)
    res = getApi(url)

    while loop is True:
        next = res.get("next")
        result = res.get('results')

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

        if next is None:
            loop = False
        else:
            res = getApi(next)

    return ''
