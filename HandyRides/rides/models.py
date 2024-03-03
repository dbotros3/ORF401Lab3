from django.db import models

# Create your models here.


class Person(models.Model):
  first_name = models.CharField(max_length=64)
  last_name = models.CharField(max_length=64)
  age = models.IntegerField()
  origination_city = models.CharField(max_length=64)
  origination_state = models.CharField(max_length=2)
  destination_city = models.CharField(max_length=64)
  destination_state = models.CharField(max_length=2)
  date = models.DateField()
  time = models.TimeField()
  taking_passengers = models.BooleanField(default=False)
  seats_available = models.IntegerField(default=0)
  email_address = models.CharField(max_length=64)
  phone_number = models.CharField(max_length=64)
  vehicle_type = models.CharField(max_length=64)
