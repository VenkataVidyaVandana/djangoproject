from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookingSerilalizer
from .models import Booking
@api_view(['GET'])
def get_bookings(request):
    bookings = Booking.objects.all()
    serializer = BookingSerilalizer(bookings, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def create_booking(request):
    serializer = BookingSerilalizer(data=request.data)

    if serializer.is_valid():
        room = serializer.validated_data['room']
        check_in = serializer.validated_data['check_in']
        check_out = serializer.validated_data['check_out']
        conflict = Booking.objects.filter(
            room=room,
            check_in=check_in,
            check_out=check_out
        )

        if conflict.exists():
            return Response(
                {'error': 'Room already booked for these dates'},
                status=400
            )
        elif(check_in >= check_out):
            return Response(
                {'error': 'Check-out date must be after check-in date'},
                status=400
            )   
            
        room.is_available = False
        room.save()

        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)