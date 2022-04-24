import datetime 
from django.db import models
from .customer import Customer
from .product import Product

class Orders(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=10, blank=True)
    date = models.DateField(default=datetime.datetime.today)
    
    