from django.db import models

# Create your models here.
class Product(models.Model):
    DELETE=0
    LIVE=1
    DELETE_CHOICE=((LIVE,'live'),(DELETE,'delete'))
    

    title=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='media/')
    priority= models.IntegerField()

    DELETE_STATUS = models.IntegerField(choices=DELETE_CHOICE, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=tuple)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


