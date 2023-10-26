from django.contrib import admin  
from django.urls import path,re_path
from django.urls import re_path as url 
from . import views  
urlpatterns = [   
    path('CustomerSignup', views.CustomerSignup),  
    path('SpSignup',views.SpSignup),  
    path('signup',views.signup),  
]  