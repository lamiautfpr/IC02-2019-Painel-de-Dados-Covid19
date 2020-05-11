from Scripts.functions import urlGeneretor, getApi
from DataBase import sqlCreator

def insertData(session):
    insertObj = sqlCreator.Insert(session)
    selectObj = sqlCreator.Select(session)
    listdate = []
    loop = True

    # date = selectObj.LastDate("date", "Brasil_api_base_mundo")
    date = "01-01-2020"
    url = urlGeneretor(4, date)
    res = getApi(url)

    while url is not None:
        next = res.get("next")
        result = res.get('data')

        for row in result:
            country = row.get('country')
            cases = row.get('cases')
            confirmed = row.get('confirmed')
            deaths = row.get('deaths')
            recovered = row.get('recovered')
            date = row.get('updated_at')
            
            listdate = [
                country,
                cases,
                confirmed,
                deaths,
                recovered,
                date
            ]
        
            insertObj.Brasilapi_mundo(listdate)
        
        if next is None:
            loop = False
        else:
            res = getApi(next)

    return ''
