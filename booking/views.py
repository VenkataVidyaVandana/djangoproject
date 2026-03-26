from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, RoomSerializer, BookingSerializer
from .models import Booking, User, Room
@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User created successfully', 'user': serializer.data}, status=201)
    return Response(serializer.errors, status=400)
@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = User.objects.filter(email = email, password = password).first()
    if user:
        return Response({'message': 'Login successful', 'user': UserSerializer(user).data}, status=200)
    return Response({'message': 'Invalid email or password'}, status=400)
#booking related apis
@api_view(['POST'])
def create_booking(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Booking created successfully', 'booking': serializer.data}, status=201)
    return Response(serializer.errors, status=400)
@api_view(['GET'])
def get_bookings(request, user_id):
    user = User.objects.filter(id = user_id).first()
    if not user:
        return Response({'message': 'User not found'}, status=404)  
    bookings = Booking.objects.filter(user = user)
    total_price = sum([b.total_price for b in bookings])
    rooms = []
    for b in bookings:
        rooms.append({
            "room_number" : b.room.room_number,
            "price" : b.room.price,
            "capacity" : b.room.capacity,
        })
    return Response({'username': user.name, 'total_price': total_price, 'rooms': rooms}, status=200)
@api_view(['DELETE'])
def delete_booking(request, id):
    user_id = request.data.get('user')
    user = User.objects.filter(id = user_id).first()
    if not user or user.role != 'admin':
        return Response({'message': 'only admin can delete bookings'}, status = 403)
    booking = Booking.objects.filter(id = id).first()
    if not booking:
        return Response({'message': 'Booking not found'}, status=404)
    booking.delete()
    return Response({'message': 'Booking deleted successfully'}, status=200)
# CRUD operations of room
@api_view(['POST'])
def room_create(request):
    serializer = RoomSerializer(data=request.data)
    user_id = request.data.get('user')
    user = User.objects.filter(id = user_id).first()
    if user.role != 'admin':
        return Response({'message': 'Only admin can create rooms'}, status=403)
    elif serializer.is_valid():
        serializer.save()
        return Response({'message': 'Room created successfully', 'room': serializer.data}, status=201)
    return Response(serializer.errors, status=400)
@api_view(['GET'])
def get_rooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data, status=200)
@api_view(['PUT'])
def update_room(request, room_number):
    user_id = request.data.get('user')
    user = User.objects.filter(id = user_id).first()
    if user.role != 'admin':
        return Response({'error': 'only admin can modify'}, status = 403)
    room = Room.objects.filter(room_number = room_number).first()
    if not room:
        return Response({'error': 'room not found'}, status = 404)
    serializer = RoomSerializer(room, data = request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Room updated successfully', 'room': serializer.data}, status=200)
    return Response(serializer.errors, status=400)
@api_view(['DELETE'])
def delete_room(request, room_number):
    user_id = request.data.get('user')
    user = User.objects.filter(id = user_id).first()
    if user.role != 'admin':
        return Response({'error': 'only admin can delete'}, status = 403)
    room = Room.objects.filter(room_number = room_number).first()
    if not room:
        return Response({'error': 'room not found'}, status = 404)
    room.delete()
    return Response({'message': 'Room deleted successfully'}, status=200)