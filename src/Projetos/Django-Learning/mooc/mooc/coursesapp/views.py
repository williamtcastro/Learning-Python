from django.shortcuts import render , get_object_or_404
from .models import Course

# Create your views here.

def index(request):
    courses = Course.objects.all()
    template_name = 'courses/index.html'
    context = { 'courses': courses }
    return render(request, template_name, context)

# use the id to populate the url
# def details(request, id):
    
#     course = get_object_or_404(Course, id=id)
#     context = { 'course': course }
#     template_name = 'courses/details.html'
#     return render(request, template_name, context)


#use the slug to populate the url
def details(request, slug):
    
    course = get_object_or_404(Course, slug=slug)
    context = { 'course': course }
    template_name = 'courses/details.html'
    return render(request, template_name, context)