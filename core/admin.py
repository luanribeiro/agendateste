from django.contrib import admin
from core.models import *
from django.db.models.base import ModelBase
from core import models

#admin.site.register(TodoList)

model_list = [m for m in dir(models) if isinstance(models.__getattribute__(m), ModelBase)]
for model_class in model_list:
    klass = models.__getattribute__(model_class)
    try:
        admin.site.register(klass)
    except:
        pass