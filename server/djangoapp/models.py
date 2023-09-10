from django.db import models
from django.core import serializers
from django.utils.timezone import now
import uuid
import json


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=100, default='Make')
    description = models.CharField(max_length=500)

    def __str__(self):
        return "Name: " + self.name

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=100, default='Car')
    id = models.IntegerField(default=1,primary_key=True)
    
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    COUPE = 'Coupe'
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe')
    ]

    type = models.CharField(
        null=False,
        max_length=50,
        choices=CAR_TYPES,
        default=SEDAN
    )
        
    year = models.DateField(default=now)

    def __str__(self):
        return "Name: " + self.name
# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(_id, _rev, id, city, state, st, address, zip, lat, long, short_name, full_name):
        # Dealer _id
        self._id = _id
        # Dealer _rev
        self._rev = _rev
        # Dealer id
        self.id = id    
        # Dealer city
        self.city = city  
        # Dealer state
        self.state = state 
        # Dealer st
        self.st = st
        # Dealer address
        self.address = address
        # Dealer zip
        self.zip = zip
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer Full Name
        self.full_name = full_name
    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
