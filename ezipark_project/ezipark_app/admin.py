from django.contrib import admin
from .models import LandOwner, ParkingSlot ,client
# Register your models here.
admin.site.register(LandOwner)
admin.site.register(ParkingSlot)
admin.site.register(client)