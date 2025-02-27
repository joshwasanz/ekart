from django.db import models
from customers.models import Customer
from products.models import Product

# Create your models here.

class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = (
        (LIVE,'LIVE'),
        (DELETE,'DELETE')
    )

    owner = models.ForeignKey(Customer,on_delete=models.SET_NULL,related_name="orders")
    delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderedItem(models.Model):
    products = models.ForeignKey(Product)
    quantity = models.IntegerField(default=1)
