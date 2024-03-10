from django.db import models

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    item_name = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)