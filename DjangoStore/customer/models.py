from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICE = ((LIVE,'live'),(DELETE,'delete'))

    name = models.CharField(max_length=200)
    address = models.TextField()
    user = models.OneToOneField(User,related_name='customer_profile', on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)

    DELETE_STATUS = models.IntegerField(choices=DELETE_CHOICE, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name