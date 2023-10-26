from django.urls import path,re_path
from django.urls import re_path as url 
from . import views

urlpatterns = [
    path('add', views.add_service),
    path('show', views.show),
    path('delete/<int:id>', views.delete),
    path('services', views.services)
]
