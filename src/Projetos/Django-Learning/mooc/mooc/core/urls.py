from django.conf.urls import url
from . import views

#AQUI VOCÊ REFERENCIA AS FUNÇÕES NAS QUAIS SERÃO CHAMADAS PELOS URLS
# NUNCA USE '' POIS ELE ENTREPRETARÁ ISSO COMO TUDO QUE FOR ESCRITO DENTRO DISSO
#SEMPRE USE '^$' PARA DETERMINAR PATHS/URLS VAZIOS

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url('contact/', views.contact, name='contact')
]