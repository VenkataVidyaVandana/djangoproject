from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('booking/create/', views.create_booking, name = 'create_booking'),
    path('room/create/', views.room_create, name = 'room_create'),
    path('room/', views.get_rooms, name = 'get_rooms'),
    path('room/update/<int:room_number>/', views.update_room, name = 'update_room'),
    path('room/delete/<int:room_number>/', views.delete_room, name = 'delete_room'),
    path('booking/<int:user_id>/', views.get_bookings, name = 'get_bookings'),
    path('booking/delete/<int:id>/', views.delete_booking, name = 'delete_booking'),
]