<<<<<<< HEAD
from Scripts.functions import urlGenerator, getApi, getNextDate, formatDate
from datetime import datetime, timedelta
=======
from Scripts.functions import now, urlGenerator, getApi, getNextDate, formatDate
>>>>>>> origin/Yoshida
from DataBase import sqlCreator

def insertData(session):

    insertObj = sqlCreator.Insert(session)
    selectObj = sqlCreator.Select(session)
<<<<<<< HEAD
    
=======

>>>>>>> origin/Yoshida
    # date = datetime(2020, 1, 29, 19, 0, 0)
    initialDate = selectObj.LastDate('datetime', '"Brasil_api_base_nacional"')

    date = getNextDate(initialDate)

    # day = datetime(2020, 1, 31, 19, 0, 0)
<<<<<<< HEAD
    now = datetime.now()
    
    # while formatDate(2, date) <= formatDate(2, day):
    while formatDate(2, date) <= formatDate(2, now):
        
=======
    day = now()

    # while formatDate(2, date) <= formatDate(2, day):
    while formatDate(2, date) <= formatDate(2, day):

>>>>>>> origin/Yoshida
        url = urlGenerator(3, formatDate(2, date))
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
<<<<<<< HEAD
            
=======

>>>>>>> origin/Yoshida
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
<<<<<<< HEAD
        
            insertObj.Brasilapi_nacional(listdate)
            
        date = getNextDate(date)

    return ''
=======

            insertObj.Brasilapi_nacional(listdate)

        date = getNextDate(date)

    return ''
>>>>>>> origin/Yoshida
