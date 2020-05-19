from Scripts.functions import urlGenerator, getApi, getNextDate, formatDate
from datetime import datetime, timedelta
from DataBase import sqlCreator

def insertData(session):

    insertObj = sqlCreator.Insert(session)
    selectObj = sqlCreator.Select(session)
    
    initialDate = selectObj.LastDate('datetime', '"Brasil_api_base_nacional"')
    
    date = getNextDate(initialDate)

    now = datetime.now()
    
    while formatDate(2, date) <= formatDate(2, now):
        
        formatedDate = formatDate(2, date)
        url = urlGenerator(3, formatedDate)
        print(url)

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