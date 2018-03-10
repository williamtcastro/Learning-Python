from django.db import models

# Create your models here.
class BusinessManager(models.QuerySet):
    def search(self, query):
        return self.filter(models.Q(name__icontains=query) | models.Q(description__icontains=query))


class BusinessAddres(models.Model):

    address = models.CharField('Endereço do Local', blank=False)
    addres_number = models.IntegerField('Numero de Endereço', max_length = 10 ,blank=False)
    city = models.CharField('Cidade do Local')

class Business(models.Model):

    name = models.CharField('Nome do Local', max_length=100 )

    address = models.CharField('Endereço do Local', blank=False)

    phone_number = models.IntegerField('Telefone do Local', blank=False)

    mobile_number = models.IntegerField('Celular do Local', blank=True)

    slug = models.SlugField('Atalho')

    description = models.TextField('Descrição Simples', max_length=200 ,blank=True )

    about = models.TextField('Sobre o Local', blank=True )

    image = models.ImageField( upload_to='myapp/images', verbose_name='Image', null=True, blank=True )

    created_at = models.DateTimeField('Criado em', auto_now_add=True )

    updated_at = models.DateTimeField('Atualizado em', auto_now=True )

    #expire_at = models.DateTimeField('Expira em', auto_now=True ) --- to be added

    objects = BusinessManager.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'Local'
        verbose_name_plural = 'Locais'
        ordering = ['name']