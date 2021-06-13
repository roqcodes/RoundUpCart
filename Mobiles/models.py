from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    category =  models.CharField(max_length=255 )
    price = models.FloatField()
    data = models.CharField(max_length=2000 )
    stock = models.IntegerField()
    image = models.CharField(max_length=2500)

# class Saled(models.Model):
#     name = 'product'
    

class Payment(models.Model):
    name = models.CharField(max_length=255 )
    email = models.EmailField()
    number = models.IntegerField(default=0)
    address = models.CharField(max_length=255 )
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.IntegerField(default=000000)

