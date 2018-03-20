from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.addBrand, name='add_vehicle'),
    #url('contact/', views.contact, name='contact')
]