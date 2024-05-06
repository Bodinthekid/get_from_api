import get_data
import send_data
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta

get_data.get_data_api()
send_data.send_data_api()

'''
def my_task():
    get_data.get_data_api()
    print("Executando minha tarefa11111111!")
    send_data.send_data_api()
    print("Executando minha tarefa!")

scheduler = BackgroundScheduler()
prox_minuto = datetime.now() + timedelta(minutes=1)

scheduler.add_job(my_task, 'date', run_date=prox_minuto)

scheduler.start()

# Imprima uma mensagem de sucesso
print("Tarefa agendada para o próximo minuto.")
'''
