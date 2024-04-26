from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Contact(models.Model):
    user = models.CharField(max_length=65)
    mail = models.CharField(max_length=65)
    phone = models.CharField(max_length=10)
    rating = models.CharField(max_length=10)
    problem = models.CharField(max_length=999)
    address = models.TextField(max_length=1000)
    def __str__ (self):
        return self.mail