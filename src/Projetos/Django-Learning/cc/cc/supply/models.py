from django.db import models

# Create your models here.
class Supply(models.Model):

    vehicle_types = (('carro', 'CARRO'),('moto', 'MOTO'),('caminhao', 'CAMINHAO'))

    vehicle_type = models.CharField(choices=vehicle_types, default='carro', max_length=100)

    # vehicleModel =

    brand = models.CharField('Marca', blank=False, max_length=100)


#---------- BRAND LIST -------------------------------