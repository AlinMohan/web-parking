from django.urls import path
from. import views
from .views import CustomLogoutView
# from django.contrib import admin
# from .views import view_parking_slots, book_slot

urlpatterns = [
    path('',views.home),
    path('home',views.home),
    path('about',views.about),
    path('register',views.register),
    path('login',views.login,name='login'),
    # path('adminlogin', admin.site.urls),
    path('registering',views.registering),
    path('loged',views.loged),
    path('logout', CustomLogoutView.as_view(), name='logout'),
    path('viewslot', views.view_parking_slots, name='view_parking_slots'),
    path('bookslot/<int:slot_id>/', views.book_slot,name='book_slot'),
    
]