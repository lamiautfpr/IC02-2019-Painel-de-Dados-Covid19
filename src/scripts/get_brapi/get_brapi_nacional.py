from scripts.functions import url_generator, get_req, next_date, format_date, now
from database import sql_creator
from datetime import datetime


def insert(session):
    print("Inserindo get_brapi_nacional.")

    insertObj = sql_creator.Insert(session)
    # selectObj = sql_creator.Select(session)
    
    date = datetime(2020, 1, 29, 19, 0, 0)
    # initialDate = selectObj.Date('datetime', '"Brasil_api_base_nacional"')
    date = next_date(date)
    # day = datetime(2020, 1, 31, 19, 0, 0)
    now = datetime.now()
    
    # while format_date(2, date) <= format_date(1, day):
    while format_date(1, date) <= format_date(1, now):
        url = url_generator(3, format_date(1, date))
        res = get_req(url)
        result = res.get('data')
        print(date)
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
        date = next_date(date)
    return print("brapi_nacional inserido com sucesso!")