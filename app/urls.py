from django.conf import settings
from django.conf.urls.static import static
from django.db import router
from xml.dom.minidom import Document
from django.urls import path , include

from app import views
urlpatterns = [
    
    path('', views.index, name='index'),
    path('hub', views.indexHub, name='hub'),
    path('contacto', views.contacto, name='contacto'),
    
]
  