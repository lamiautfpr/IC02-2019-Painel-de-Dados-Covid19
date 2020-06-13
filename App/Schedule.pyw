import schedule
import time
import insertData
from datetime import datetime

def job():
    
    insertData.insertAll()
    print("Dados inseridos com sucesso. Datetime {}".format(datetime.now()))

    return

schedule.every().day.at("11:36").do(job)
schedule.every().day.at("23:00").do(job)

while True:
    schedule.run_pending()

    time.sleep(10)