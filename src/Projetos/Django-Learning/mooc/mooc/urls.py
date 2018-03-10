"""mooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#DEBUG MODE
from django.conf import settings
from django.conf.urls.static import static

#AQUI VOCÊ REFERENCIA OS PATHS QUE SERÃO PASSADOS AOS URLS.PY DOS APPS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mooc.core.urls'), name='home'),
    path('courses/', include('mooc.coursesapp.urls'), name='courses')
]


#show images on the debug mode on
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)