from django.db import models

# Create your models here.


class Person(models.Model):
  first_name = models.CharField(max_length=64)
  last_name = models.CharField(max_length=64, default="Smith")
  age = models.IntegerField(default=21)
  origination_city = models.CharField(max_length=64, default="Princeton")
  origination_state = models.CharField(max_length=2, default="NJ")
  destination_city = models.CharField(max_length=64)
  destination_state = models.CharField(max_length=2)
  date = models.DateField()
  time = models.TimeField()
  taking_passengers = models.BooleanField(default=False)
  seats_available = models.IntegerField(default=0)
  email_address = models.CharField(max_length=64, default="@princeton.edu")
  vehicle_type = models.CharField(max_length=64, default="Tesla")
