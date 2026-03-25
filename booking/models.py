from django.db import models
class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Room(models.Model):
    room_number = models.IntegerField()
    price = models.IntegerField()
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return f"Room {self.room_number}"
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    def __str__(self):
        return f"Booking for {self.user.name} in Room {self.room.room_number}"
