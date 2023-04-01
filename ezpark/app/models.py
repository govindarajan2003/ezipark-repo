from django.db import models

# Create your models here.
class Client(models.Model):
  
  c_id= models.AutoField(primary_key= True)
  email= models.CharField(max_length=100)
  full_name = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  booking_status= models.CharField(max_length=100)
  fine = models.IntegerField(default = 0) 

  def __str__(self):
    return f"{self.full_name}"

class LandOwner(models.Model):
  la_id = models.AutoField(primary_key= True)
  email = models.CharField(max_length=100)
  full_name = models.CharField(max_length= 100)
  phone = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  booking_status= models.CharField(max_length=100)
  pincode = models.CharField(max_length=100)
  landmark = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.full_name}"

class Land(models.Model):

  l_id = models.AutoField(primary_key= True)
  pincode = models.IntegerField(max_length=100)
  sq_feet = models.FloatField(default=0)
  booking_status = models.CharField(max_length=100)

  
class Vehicle(models.Model):
  v_id = models.AutoField(primary_key=True)
  v_number = models.CharField(max_length=100)
  v_type = models.CharField(max_length=100)
  
class Booking(models.Model):
  B_id = models.AutoField(primary_key=True)
  booking_status = models.CharField(max_length=100)


