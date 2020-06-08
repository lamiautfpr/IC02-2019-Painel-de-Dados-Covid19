from Scripts.functions import getApi, urlGenerator
from DataBase import sqlCreator
import json
from datetime import datetime, timedelta
DROPDAYS = 10

def insertData(session):
    insertObj = sqlCreator.Insert(session)
    selectObj = sqlCreator.Select(session)
    deleteObj = sqlCreator.Delete(session)

    last_date = selectObj.LastDate("date", "Brasil_io_base_nacional")   #última data de inserção
    url = urlGenerator(1)
    response = getApi(url)
    updated = False
    date_start_str = last_date.strftime("%Y-%m-%d")     #preenche da data mais atual (last_date) para a mais antiga (apagada)
    date_end = (last_date - timedelta(days=DROPDAYS))   #datetime
    date_end_str = date_end.strftime("%Y-%m-%d")        #string

    #Deleta DROPDAYS dias para trás e reinsere no banco
    deleteObj.DeletePeriod("Brasil_io_base_nacional","date", date_start_str, date_end_str) #falta datetime2

    while url is not None and not updated:      #updated = quando dados estiverem atualizados
        listdate = []
        result = response.get('results')
        for row in result:
            date = row.get('date')
            if last_date is None:
                pass
            elif datetime.strptime(date, '%Y-%m-%d').date() <= date_end:
                updated = True
                break
            city = row.get('city')
            ibge_code = row.get('city_ibge_code')
            confirmed = row.get('confirmed')
            confirmed_100k = row.get('confirmed_per_100k_inhabitants')            
            death_rate = row.get('death_rate')
            deaths = row.get('deaths')
            population = row.get('estimated_population_2019')
            is_last = row.get('is_last')
            place_type = row.get('place_type')
            state = row.get('state')
            listdate = [
                city,
                ibge_code,
                confirmed,
                confirmed_100k,
                date,
                death_rate,
                deaths,
                population,
                is_last,
                place_type,
                state
            ]
            insertObj.Brasilio_nacional(listdate)

        if not updated:
            url = response.get('next')
            if url:
                response = getApi(url)

    return ''
