from django.shortcuts import render
from .models import Supply
from . import brandList as bL
 
# Create your views here.
def addBrand(request):
    vehicle_type = str(request.POST.get('Tipo'))
    car_brands = bL.vehicleBrands(vehicle_type)
    context = { 'brands': car_brands }
    template_name = 'addvehicle.html'

    return render(request, template_name, context)