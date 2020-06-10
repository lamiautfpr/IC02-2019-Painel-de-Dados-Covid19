from Scripts.functions import now, urlGenerator, getApi, getNextDate, formatDate
from DataBase import sqlCreator
from datetime import datetime

def insertData(session):

    print("Coletando e inserindo dados para Brasil-api-base-nacional...")

    insertObj = sqlCreator.Insert(session)
    selectObj = sqlCreator.Select(session)

    # date = datetime(2020, 1, 29, 19, 0, 0)
    initialDate = selectObj.LastDate('datetime', '"Brasil_api_base_nacional"')

    date = getNextDate(initialDate)

    # day = datetime(2020, 1, 31, 19, 0, 0)
    day = now()

    # while formatDate(2, date) <= formatDate(2, day):
    while formatDate(2, date) <= formatDate(2, day):

        url = urlGenerator(3, formatDate(2, date))

        res = getApi(url)
        result = res.get('data')

        for row in result:
            uid = row.get('uid')
            uf = row.get('uf')
            state = row.get('state')
            cases = row.get('cases')
            deaths = row.get('deaths')
            suspects = row.get('suspects')
            refuses = row.get('refuses')
            datet = row.get('datetime')

            listdate = [
                uid,
                uf,
                state,
                cases,
                deaths,
                suspects,
                refuses,
                datet
            ]

            insertObj.Brasilapi_nacional(listdate)

        date = getNextDate(date)

    return ''
