import datetime 
from django.db import models
from .customer import Customer
from .product import Product
from .status import Status

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=100)
    address = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=10, blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.ForeignKey(Status, default=Status(1), on_delete=models.CASCADE)
    
    
    def placeOrder(self):
        self.save()
    
    
    @staticmethod
    def get_order_by_customer(customerId):
        return Order.objects.filter(customer = customerId)