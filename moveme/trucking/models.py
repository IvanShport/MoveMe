import datetime
from django.db import models, IntegrityError
from django.utils import timezone
from django.http import Http404
from django.contrib.auth.models import User
from user.models import Profile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class Order(models.Model):
    destination_country = models.CharField(max_length = 64)
    departure_country = models.CharField(max_length = 64)
    destination_city = models.CharField(max_length = 64)
    departure_city = models.CharField(max_length = 64)
    destination_street = models.CharField(max_length = 64)
    departure_street = models.CharField(max_length = 64)
    destination_house = models.CharField(max_length = 64)
    departure_house = models.CharField(max_length = 64)
    destination_details = models.CharField(max_length = 64)
    departure_details = models.CharField(max_length = 64)
    buyer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    cost = models.CharField(max_length = 32)

    def __str__(self):
        return self.id

class Driver(models.Model):
    name = models.CharField(max_length = 128)
    phone_number = models.CharField(max_length = 64)
    passport_data = models.CharField(max_length = 128)
    
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    type_auto = models.CharField(max_length = 64)
    model = models.CharField(max_length = 64)
    capacity_weight = models.IntegerField(default=0)
    capacity_volume = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null = True)
    driver = models.OneToOneField(Driver, on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return self.model





