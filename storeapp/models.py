from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Suppliers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to="")
    type = models.CharField(max_length=15)
    status = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    def __str__ (self):
        return self.user.username

class Items(models.Model):
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    itemname = models.CharField(max_length=200)
    itemprice = models.FloatField()
    itemimage = models.ImageField(upload_to="")
    itemcategary = models.CharField(max_length=100)
    itemstockquantity = models.IntegerField()
    itemdescription = models.CharField(max_length=1000)
    itemrating = models.FloatField()

    def __str__ (self):
        return self.itemname