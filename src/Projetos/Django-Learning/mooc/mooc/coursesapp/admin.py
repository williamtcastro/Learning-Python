from django.contrib import admin
from .models import Course

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    
    #edit admin list of the main display
    list_display = ['name', 'slug', 'start_date', 'created_at']

    #add search bars for the admin oage
    search_fields = ['name', 'slug']

    #auto populate fields with the slug forms
    prepopulated_fields={'slug':['name']}

admin.site.register(Course, CourseAdmin)