import main
import schedule
import time
from scripts.functions import now

def job():
    main.insert_all()
    return print("Dados inseridos com sucesso. Datetime {}".format(now()))

schedule.every().day.at("11:59").do(job)
schedule.every().day.at("19:30").do(job)
schedule.every().day.at("23:59").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)