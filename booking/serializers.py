from .models import User, Room, Booking
from rest_framework import serializers
class BookingSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'