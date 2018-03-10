from django.db import models

# Create your models here.
class Supply(models.Model):

    vehicleTypes = (('carro', 'CARRO'),('moto', 'MOTO'),('caminhao', 'CAMINHAO'))

    vehicleType = models.CharField(choices=vehicleTypes, default='carro')

    brand = models.CharField('Marca', blank=False)


#---------- BRAND LIST -------------------------------