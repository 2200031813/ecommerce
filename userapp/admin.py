from django.contrib import admin

from .models import UsersData, Cart, Bookings

# Register your models here.
admin.site.register(UsersData)
admin.site.register(Cart)
admin.site.register(Bookings)