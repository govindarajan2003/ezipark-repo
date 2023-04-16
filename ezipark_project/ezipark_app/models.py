from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class LandOwner(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    contact_number = models.CharField(max_length=15)
    
class ParkingSlot(models.Model):
    LandOwner =models.ForeignKey(LandOwner, on_delete= models.CASCADE)
    address = models.CharField(max_length=255)
    pincode = models.CharField(max_length=6)
    available = models.BooleanField(default=True)

class client(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    contact_number = models.CharField(max_length=15)

