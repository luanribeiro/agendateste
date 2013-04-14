
from django.conf.urls import patterns, url

urlpatterns = patterns('core.views',
    #agenda
    url(r'^/?$', view='index', name='index'),
    url(regex=r'^add/?$', view='add', name='add'),
    # url(
    #     regex=r'^edit/todolist/(?P<slug>\w+)/$',
    #     view='edit',
    #     name='edit'
    # ),
    # url(
    #     regex=r'^delete/todolist/(?P<slug>\w+)/$',
    #     view='delete',
    #     name='delete'
    # ),
)