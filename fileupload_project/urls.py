"""
URL configuration for fileupload_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from accounts import views
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path ,include
from django.conf.urls.static import static 
from django.conf import settings
urlpatterns = [
     path('', views.custom_login, name='custom_login'),
     path('grappelli/', include('grappelli.urls')),  # grappelli URL
     path('admin/', admin.site.urls),
     path('upload', include('uploader.urls')),#  conflict kar rha hai 
  #   path('', TemplateView.as_view(template_name='login.html')), conflict karega user/login se 
     path('register/', views.register, name='register'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)