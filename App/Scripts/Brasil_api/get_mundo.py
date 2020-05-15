from Scripts.functions import now, urlGenerator, getApi, formatDate
from DataBase import sqlCreator


def insertData(session):

    selectObj = sqlCreator.Select(session)
    date = selectObj.LastDate('updated_at', '"Brasil_api_base_mundo"')

    day = now()

    if formatDate(2, date) != formatDate(2, day):
        url = urlGenerator(4, '')
        res = getApi(url)

        result = res.get('data')

        insertObj = sqlCreator.Insert(session)

        for row in result:
            country = row.get('country')
            cases = row.get('cases')
            confirmed = row.get('confirmed')
            deaths = row.get('deaths')
            recovered = row.get('recovered')
            updated_at = row.get('updated_at')

            listdate = [
                country,
                cases,
                confirmed,
                deaths,
                recovered,
                updated_at
            ]

            insertObj.Brasilapi_mundo(listdate)
    else:
        print("Updated data are up to date.")

    return ''
