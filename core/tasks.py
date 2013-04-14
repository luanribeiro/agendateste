from celery.task.schedules import crontab
from celery.decorators import periodic_task

from core.models import *

from datetime import *

from django.core.mail import send_mail

# this will run every minute, see http://celeryproject.org/docs/reference/celery.task.schedules.html#celery.task.schedules.crontab
@periodic_task(run_every=crontab(hour="*", minute="*/2", day_of_week="*"))
def test():    
    data =  datetime.today()
    atividades = Atividade.objects.all()
    for atividade in atividades :
        if (data.date() == atividade.horario.date()) :
            titulo = 'Lembrete de Atividade';
            msg = 'Hoje tem uma atividade marcada para hoje.\n\n%s\n\n%s' % (atividade.nome , atividade.descricao)

            print 'Enviando email'
            send_mail(subject=titulo, message=msg, from_email='luantribeiro@gmail.com',
                    recipient_list=['luantribeiro@gmail.com'])
            print 'Email enviado'


    # print "Tarefa de teste HAHAHA..."