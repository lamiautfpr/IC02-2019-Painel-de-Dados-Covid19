import schedule
import time
import insertData
from datetime import datetime

def job():
    
    insertData.insertAll()
    print("Dados inseridos com sucesso. Datetime {}".format(datetime.now()))

schedule.every().day.at("11:30").do(job)
schedule.every().day.at("23:30").do(job)

while True:
    schedule.run_pending()

    time.sleep(10)