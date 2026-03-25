from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('bookings/', views.get_bookings, name='get_bookings'),
    path('create/', views.create_booking, name='create_booking'),  
]