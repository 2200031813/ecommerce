from django.contrib.auth.models import User
from django.db import models

from storeapp.models import Items

from storeapp.models import Suppliers


# Create your models here.
class UsersData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to="")
    type = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    def __str__ (self):
        return self.user.username



class Bookings(models.Model):
    supplier = models.ForeignKey(Suppliers, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Items, on_delete=models.SET_NULL, null=True)
    bookinguser = models.ForeignKey(UsersData, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    applydate = models.DateField()
    applytime = models.TimeField()
    status= models.TextField(max_length=99)
    def __str__ (self):
        return str(self.bookinguser)

class Cart(models.Model):
    supplier = models.CharField(max_length=100)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    bookinguser = models.ForeignKey(UsersData, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__ (self):
        return str(str(self.bookinguser)+"    "+str(self.item))


class Payment(models.Model):
    bookinguser = models.ForeignKey(UsersData, on_delete=models.CASCADE)
    amount=models.CharField(max_length=100)
    order_id = models.CharField(max_length=100,blank=True)
    razorpay_payment_id = models.CharField(max_length=100,blank=True)
    paid = models.BooleanField(default=False)