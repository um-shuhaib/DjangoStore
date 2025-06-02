from django.db import models
from customer.models import Customer
from product.models import Product

# Create your models here.



class Orders(models.Model):
    LIVE=1
    DELETE = 0
    DELETE_CHOICE = ((LIVE,'live'),(DELETE,'delete'))

    owner = models.ForeignKey(Customer,related_name='order',on_delete=models.SET_NULL, null=True)

    DELETE_STATUS = models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELEVERED = 3
    ORDER_REJECTED = 4
    STATUS_CHOICE = (
        (ORDER_PROCESSED,'order_processed'),
        (ORDER_DELEVERED,'ordef_delivered'),
        (ORDER_REJECTED,'order_rejected')
    )
    ORDEER_STATUS = models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)



class OrderItem(models.Model):
    product = models.ForeignKey(Product,related_name='added_cart',on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Orders,related_name='added_items',on_delete=models.CASCADE)
