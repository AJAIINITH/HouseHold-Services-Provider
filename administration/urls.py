from django.urls import path,re_path
from django.urls import re_path as url 
from . import views


urlpatterns = [
    path('show/<str:type>', views.show),
    path('delete/<str:type>,<str:id>', views.delete),
]
