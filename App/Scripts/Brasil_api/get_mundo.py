from Scripts.functions import now, urlGenerator, getApi, formatDate
from DataBase import sqlCreator
from datetime import datetime

def insertData(session):
    
    print("Coletando e inserindo dados para Brasil-api-base-mundo...")

    selectObj = sqlCreator.Select(session)
    date = selectObj.LastDate('updated_at', '"Brasil_api_base_mundo"')
    # date = datetime(2020, 1, 29, 19, 0, 0) 
    
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
<<<<<<< HEAD
            
=======

>>>>>>> origin/Yoshida
            listdate = [
                country,
                cases,
                confirmed,
                deaths,
                recovered,
                updated_at
            ]
<<<<<<< HEAD
        
=======

>>>>>>> origin/Yoshida
            insertObj.Brasilapi_mundo(listdate)
    else:
        print("Os dados da Brasil-api-base-mundo já estão atualizados.")

<<<<<<< HEAD
    return ''
=======
    return ''
>>>>>>> origin/Yoshida
