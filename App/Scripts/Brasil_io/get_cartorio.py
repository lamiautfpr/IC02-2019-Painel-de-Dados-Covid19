from Scripts.functions import urlGeneretor, getApi
from DataBase import sqlCreator


def insertData(session):
    insertObj = sqlCreator.Insert(session)
    selectObj = sqlCreator.Select(session)
    listdate = []
    loop = True

    # date = selectObj.LastDate("date", "Brasil_io_base_cartorio")
    date = "01-01-2020"
    url = urlGeneretor(1, date)
    res = getApi(url)

    while url is not None:
        next = res.get("next")
        result = res.get('results')

        for row in result:
            date = row.get('date')

            listdate = [
                ""
            ]
            insertObj.Brasilio_cartorio(listdate)

        if next is None:
            loop = False
        else:
            res = getApi(next)

    return ''
