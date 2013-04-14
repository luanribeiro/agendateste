# Create your views here.
from django.shortcuts import (render_to_response, redirect)
from django.template import RequestContext
from core.models import *
from core.forms import AtividadeForm
from datetime import *

from django.core.mail import send_mail


def index(request):
    data =  datetime.today()
    atividades = Atividade.objects.all()
    # for atividade in atividades :
    #     print data.date()
    #     print atividade.horario.date()
    #     print (data.date() == atividade.horario.date())

    data = {
        'atividades' : atividades
    }
    return render_to_response('index.html', data,
            context_instance=RequestContext(request))


def add(request) :
    ativiadeForm = AtividadeForm(request.POST or None)

    if ativiadeForm.is_valid() :
        addAtividade(ativiadeForm, request)
        return redirect('index')

    data = {
        'atvForm' : ativiadeForm
    }
    return render_to_response('add.html', data,
            context_instance=RequestContext(request))


#   Adiciona a atividade e envia um email
def addAtividade(atividadeForm, request) :
    atividadeForm.save()

    titulo = 'Atividade Adicionada';
    msg = 'Voce tem uma nova atividade para o dia %s. A mensagem eh: %s' % (request.POST.get('horario') , request.POST.get('descricao'))

    send_mail(subject=titulo, message=msg, from_email='luantribeiro@gmail.com',
            recipient_list=['luantribeiro@gmail.com'])
