from Scripts.functions import urlGeneretor, getApi
from DataBase import sqlCreator

def insertData(session):
    insertObj = sqlCreator.Insert(session)
    selectObj = sqlCreator.Select(session)
    listdate = []
    loop = True

    # date = selectObj.LastDate("date", "Brasil_api_base_nacional")
    date = "20200131"
    url = urlGeneretor(3, date)
    res = getApi(url)

    while url is not None:
        next = res.get("next")
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
        
        if next is None:
            loop = False
        else:
            res = getApi(next)

    return ''
