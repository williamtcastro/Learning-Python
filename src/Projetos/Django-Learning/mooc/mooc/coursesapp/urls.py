from django.conf.urls import url
from . import views

#AQUI VOCÊ REFERENCIA AS FUNÇÕES NAS QUAIS SERÃO CHAMADAS PELOS URLS
# NUNCA USE '' POIS ELE ENTREPRETARÁ ISSO COMO TUDO QUE FOR ESCRITO DENTRO DISSO
#SEMPRE USE '^$' PARA DETERMINAR PATHS/URLS VAZIOS

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^(?P<id>\d+)/$', views.details, name='details')
    url(r'^(?P<slug>[\w_-]+)/$', views.details, name='details')
]