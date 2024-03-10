from django.db import models

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import datetime


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
class Sub_Category(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=False,default='')
    sub_category = models.ForeignKey(Sub_Category,on_delete=models.CASCADE,null=False,default='')
    image = models.ImageField(upload_to='ecommerce/pimg')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True,label='Email',error_messages={'exists':'This Already Exists'})

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm Password'
    def save(self, commit=True):
        user = super(UserCreateForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_message['exists'])
        return self.cleaned_data['email']


class Order(models.Model):
    image = models.ImageField(upload_to= 'ecommerce/order/image')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.CharFiels()
    price = models.ImageField()
    address = models.TextField()
    phone = models.CharField(max_length=10)
    pincode = models.CharField(max_length=10)
    date = models.DateField(default=datetime.datetime.today)

class Feedback(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    feedback_text = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"