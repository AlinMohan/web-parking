from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('',views.home),
    path('home',views.home),
    path('about',views.about),
    path('register',views.register),
    path('login',views.login),
    path('adminlogin', admin.site.urls),
    path('registering',views.registering),
    path('loged',views.loged),
]