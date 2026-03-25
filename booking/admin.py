from django.contrib import admin
from .models import user, room, booking
admin.site.register(user)
admin.site.register(room)
admin.site.register(booking)

# Register your models here.
