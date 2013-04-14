from django.db import models

# Create your models here.

class Atividade(models.Model):

    nome = models.CharField(
        max_length = 100, 
        null = False
    )
    
    descricao = models.CharField(
        max_length = 255, 
        null = False
    )

    horario = models.DateTimeField(
        null = False
    )

    def __unicode__(self):
        return u"%s" % self.nome




