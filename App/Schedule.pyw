import schedule
import time
import insertData
from datetime import datetime

def job():
    
    insertData.insertAll()
    print("Dados inseridos com sucesso. Datetime {}".format(datetime.now()))

    return

schedule.every().day.at("00:18").do(job)

while True:
    schedule.run_pending()

    time.sleep(10)