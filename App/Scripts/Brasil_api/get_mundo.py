from Scripts.functions import urlGenerator, getApi
from DataBase import sqlCreator

def insertData(session):

    insertObj = sqlCreator.Insert(session)
    selectObj = sqlCreator.Select(session)
    
    date = ''

    url = urlGenerator(4, date)
    res = getApi(url)

    result = res.get('data')

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

    return ''