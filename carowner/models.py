
#<<<<<<< HEAD

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class CarOwnerProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=256, default=None, null=True, blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('owner-view')
# Create your models here.
class Car(models.Model):
    TRANSMISSION_TYPES = (
        ('AUTO', 'auto'),
        ('MANUAL', 'manual')
    )
    BODY_TYPES = (
        ('S', 'Sedan'),
        ('C', 'Coupe'),
        ('W', 'Wagon'),
        ('CV', 'Convertible'),
        ('CP', 'Coupe'),
        ('HB', 'Hatchback'),
        ('T', 'Truck'),
        ('UTE', 'Ute'),
        ('S', 'Sedan'),
        ('SUV', 'SUV'),
        ('VAN', 'Van'),
        ('W', 'Wagon'),
        ('OTHER', 'Other'),
    )

    COLOUR_TYPES = (
        ('W', 'White'),
        ('S', 'Silver'),
        ('BK', 'Black'),
        ('BL', 'Blue'),
        ('GRY', 'Grey'),
        ('R', 'Red'),
        ('BRZ', 'Bronze'),
        ('BRN', 'Brown'),
        ('BUR', 'Burgundy'),
        ('C', 'Cream'),
        ('GD', 'Gold'),
        ('GRN', 'Green'),
        ('O', 'Orange'),
        ('PK', 'Pink'),
        ('PU', 'Purple'),
        ('Y', 'Yellow'),
        ('OTHER', 'Other'),
    )

    TRANSMISSION_TYPES = (
        ('AUTO', 'automatic'),
        ('MANUAL', 'manual'),
    )

    FUEL_TYPES = (
        ('D', 'Diesel'),
        ('P', 'Petrol'),
    )
    owner = models.ForeignKey(CarOwnerProfile, on_delete=models.CASCADE)
    make = models.CharField(max_length=256, default=None, null=True, blank=True)
    # model =
    body_type = models.CharField(max_length=256, default=None, null=True, blank=True)
    transmission = models.CharField(max_length=256, choices=TRANSMISSION_TYPES)
    comments = models.TextField(default=None, null=True, blank=True)
    series = models.CharField(max_length=256, default=None, null=True, blank=True)
    seats = models.IntegerField(default=None, null=True, blank=True)
    colour = models.CharField(max_length=256,default=None, null=True, blank=True)
    registration_number = models.CharField(max_length=256, default=None, null=True, blank=True)
    fuel_type = models.CharField(max_length=256, choices=FUEL_TYPES, default=None, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('car-view')

    def __str__(self):
        return self.owner.name

class Earning(models.Model):
    owner = models.ForeignKey(CarOwnerProfile, on_delete=models.CASCADE,null=True)
    balance = models.IntegerField(default=None,null=True,blank=True)

class Rating(models.Model):
    owner = models.ForeignKey(CarOwnerProfile, on_delete=models.CASCADE,null=True)
    carcomment = models.CharField(max_length=256, default=None, null=True, blank=True)



