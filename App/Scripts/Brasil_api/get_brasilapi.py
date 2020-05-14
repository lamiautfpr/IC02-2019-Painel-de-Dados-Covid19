from Scripts.functions import urlGenerator, getApi, getNextDate, formatDate
from datetime import datetime, timedelta
from DataBase import sqlCreator

def insertData(session):
    selectObj = sqlCreator.Select(session)
    initialDate = selectObj.LastDate('datetime', '"Brasil_api_base_nacional"')
    date = getNextDate(initialDate)
    
    now = datetime.now()

    while date != now:
        temp_date = formatDate(2, date)
        
        url = urlGenerator(3, temp_date)
        res = getApi(url)

        result = res.get('data')

        insertObj = sqlCreator.Insert(session)

        for row in result:
            uid = row.get('uid')
            uf = row.get('uf')
            state = row.get('state')
            cases = row.get('cases')
            deaths = row.get('deaths')
            suspects = row.get('suspects')
            refuses = row.get('refuses')
            date = row.get('datetime')
            
            listdate = [
                uid,
                uf,
                state,
                cases,
                deaths,
                suspects,
                refuses,
                date
            ]
        
            insertObj.Brasilapi_nacional(listdate)

        date = getNextDate(date)
        
    return ''

def test(session):

    insertObj = sqlCreator.Insert(session)
    selectObj = sqlCreator.Select(session)
    
    initialDate = datetime(2020, 1, 30, 19, 0, 0)
    now = datetime.now()
    date = getNextDate(initialDate)

    while formatDate(2, date) <= formatDate(2, now):
        
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
            date = row.get('datetime')
            
            listdate = [
                uid,
                uf,
                state,
                cases,
                deaths,
                suspects,
                refuses,
                date
            ]
        
            insertObj.Brasilapi_nacional(listdate)

        date = getNextDate(date)

    return ''