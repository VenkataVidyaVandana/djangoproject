from rest_framework import serializers
from .models import User, Room, Booking
class UserSerializer(serializers.ModelSerializer):
    def validate_email(self, value):
        if User.objects.filter(email = value).exists():
            raise serializers.ValidationError("email already exists")
        return value
    class Meta:
        model = User
        fields = '__all__'
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
class BookingSerializer(serializers.ModelSerializer):
    def validate(self,data):
        if(data['check_in']>= data['check_out']):
            raise serializers.error("checkin date must be less than check out")
        conflict = Booking.objects.filter(room = data['room'], check_in = data['check_in'], check_out = data['check_out'])
        if conflict.exists():
            raise serializers.error("room is already booked for the selected dates")
        return data
    #pricing logic
    def create(self, validated_data):
        room = validated_data['room']
        check_in = validated_data['check_in']
        check_out = validated_data['check_out']
        days = (check_out- check_in).days
        total = days * room.price
        validated_data['total_price'] = total
        return super().create(validated_data)
    class Meta:
        model = Booking
        fields = '__all__'
