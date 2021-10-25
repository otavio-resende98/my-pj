import datetime
import time

from django.utils.timezone import now
from celery.decorators import task, periodic_task
from celery.utils.log import get_task_logger
from celery import shared_task
from celery.task.schedules import crontab

from .models import Activity
from config.settings.base import ( BUSINESS_TIMEOUT_HOUR,
                                   BUSINESS_TIMEOUT_MINUTE,
                                   BUSINESS_MAX_UNCLOSED_ACTIVITY,
                                   BUSINESS_RG_END_HOUR,
                                   BUSINESS_RG_END_MINUTE,
                                   BUSINESS_RG_WEEK_DAY,)

import os
#Rodar Cron
from django.core import management
from django.conf import settings
#from django_cron import CronJobBase, Schedule

logger = get_task_logger(__name__)

""" Task para identificação de pontos não fechados """
def check_for_missed_outs(activity_id):
    current_time = now()
    end_time = current_time + datetime.timedelta(
            hours=BUSINESS_MAX_UNCLOSED_ACTIVITY)

    while (current_time < end_time and 
            (current_time.hour <= BUSINESS_TIMEOUT_HOUR and
            current_time.minute < BUSINESS_TIMEOUT_MINUTE)):
        print("Entrou no while")
        activity = Activity.objects.filter(pk=activity_id).first()
        if activity.hour_end is not None:
            print("hour_end setada. Encerrando task...")
            return False
        time.sleep(60)
        current_time = now()
    print("Deleting activity:", activity)
    activity.delete()
    return True
@task(name="check_for_missed_outs_task")
def check_for_missed_outs_task(activity_id):
    logger.info("Iniciada nova thread")
    status = check_for_missed_outs(activity_id)
    return {"status": status}

#################################################################################
""" Task para identificação de ausências em RG """
##PSEUDO CÓDIGO##
def get_rg_absenses(): #recebe um vetor de id presente na reunião
    print("ABSENSES HERE!")
@periodic_task(
    run_every=(crontab(hour=18 + 3,  # ajuste no UTC
                       minute=30,
                       day_of_week='wed')),
    name="get_rg_absenses_task",
    ignore_result=True
)
def get_rg_absenses_task():
    #se for traine
      #enviar e-mail para diretor de processo interno
      #passar como parametro nome do trainee
    #senao se for membro e ausente em duas reuniões
      #enviar e-mail para membro com advertencia
    get_rg_absenses()


##############################################################################
""" Task para envio de horas cumpridas e ocasionais advertências de
    membros, trainees e admin """
def send_completed_hours():#Buscar dados no banco de dados
    #dados horas de trainee e membros
    pass
@periodic_task(
    run_every=(crontab(hour=23,  # + 3 ajuste no UTC
                       minute=59,
                       day_of_week='fri')),
    name="send_completed_hours_task",
    ignore_result=True
)
def send_completed_hours_task():
  #se trainee e  menor que 1 hr
    #enviar email diretor de processo interno
  #se trainee e menor que 4 hr
    #enviar email para o membro
  #enviar para tds as hrs cumpridas
  #zerar tds as horas
  pass



#Task para fazer Backup
@periodic_task(
  run_every=(crontab(hour=18+3,minute=5)),
  name="backup_done_task",
  ignore_result=True
)
def backup_done_task():
  management.call_command('dbbackup') #Essa linha executa um comando direto que é parecido com python manage.py dbbackup

#Rodar backup com Cron#
#class Backup(CronJobBase):
#  RUN_AT_TIMES = ['6:00', '18:00']
#  schedule = Schedule(run_at_times=RUN_AT_TIMES)
#  code = 'my_app.Backup'
#  def do(self):
#    management.call_command('dbbackup')