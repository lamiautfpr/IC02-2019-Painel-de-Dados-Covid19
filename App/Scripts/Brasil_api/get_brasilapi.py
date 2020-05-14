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

def urlGenerator(var, date):
    if var == 1:
    #Brasil.ioNacional
        url = ('https://brasil.io/api/dataset/covid19/caso/data/?date<{}'
            .format(date))
    elif var == 2:
    #Brasil.ioCartorio
        url = ('https://brasil.io/api/dataset/covid19/obito_cartorio/data/?date<{}'
            .format(date))
    elif var == 3:
    #Brasil.apiNacional
        url = ('https://covid19-brazil-api.now.sh/api/report/v1/brazil/{}'
            .format(date))
    elif var == 4:
    #Brasil.apiMundial
        url = ('https://covid19-brazil-api.now.sh/api/report/v1/countries')
    else:
        pass

    return url

def formatDate(var, date):
    
    if var == 1:
    #Brasil.io
        pass
    elif var == 2:
    #Brasil.api
        date = date.strftime('%Y%m%d')
    else:
        pass
    
    return date

def getNextDate(date):

    date += timedelta(1)
    
    return date

def test():

    selectObj = sqlCreator.Select(session)
    initialDate = datetime(selectObj.LastDate('datetime', '"Brasil_api_base_nacional"'))
    now = datetime.now()
    date = getNextDate(initialDate)

    while formatDate(2, date) <= formatDate(2, now):
        print(urlGenerator(3, formatDate(2, date)))
        date = getNextDate(date)

    return ''

test()