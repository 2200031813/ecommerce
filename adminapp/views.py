from django.conf import settings
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from storeapp.models import Suppliers, Items

from userapp.models import Bookings

from userapp.models import UsersData

from .models import Contact


# Create your views here.
def adminpannelindex(request):
    return render(request,"adminpannelapp/adminpannelindex.html")

def adminlogout(request):
    logout(request)
    return redirect('index')

def adminpannellogin(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user.is_superuser:
            login(request, user)
            return redirect('adminpannelindex')
    return render(request,"adminpannelapp/adminpannellogin.html")

def Allitemsadmin(request):
    items=Items.objects.all()
    return render(request, "adminpannelapp/Allitems.html",{"items":items})

def AllSuppliers(request):
    farmers=Suppliers.objects.all();
    return render(request, "adminpannelapp/AllSuppliers.html",{"farmers":farmers})

def Allusers(request):
    users = UsersData.objects.all();
    return render(request, "adminpannelapp/Allusers.html", {"users": users})

def Suppliersstatus(request,ram):
    farmer=Suppliers.objects.get(id=ram)
    if request.method=="POST":
        farmer.status=request.POST['status']
        farmer.save()
        # a=request.POST['status']
        # mail = farmer.user.email
        # if a=="Accepted":
        #     tosend = 'From Team SUPPORT TO FARMERS \nYou are Accepted By the team '
        # else:
        #     tosend = 'From Team SUPPORT TO FARMERS \n You are Rejectd By the team\n Better Luck next Time'
        # send_mail(
        #     'From The Team SUPPORT TO FARMERS',
        #     tosend,
        #     settings.EMAIL_HOST_USER,
        #     [mail],
        #     fail_silently=False,
        # )
        return redirect("AllSuppliers")
    return render(request,"adminpannelapp/Suppliersstatus.html",{"farmer":farmer})

def Suppliersdelete(request,ram):
    farmer = Suppliers.objects.get(id=ram)
    User.objects.get(id=farmer.user.id).delete()
    return redirect("AllSuppliers")

def AllAcceptedSuppliers(request):
    farmers=Suppliers.objects.filter(status="Accepted");
    return render(request, "adminpannelapp/AllSuppliers.html",{"farmers":farmers})


def AllRejectedSuppliers(request):
    farmers=Suppliers.objects.filter(status="Rejected");
    return render(request, "adminpannelapp/AllSuppliers.html",{"farmers":farmers})


def AllPendingSuppliers(request):
    farmers=Suppliers.objects.filter(status="pending");
    return render(request, "adminpannelapp/AllSuppliers.html",{"farmers":farmers})


def AllCanceledItems(request):
    itemsbooked=Bookings.objects.filter(status="Canceled").order_by('-applydate', 'applytime')
    return render(request, "adminpannelapp/AllorderedItems.html", {'items': itemsbooked})

def AllDeliveredItems(request):
    itemsbooked=Bookings.objects.filter(status="Delivered").order_by('-applydate', 'applytime')
    return render(request, "adminpannelapp/AllorderedItems.html", {'items': itemsbooked})

def AllNotDeliveredItems(request):
    itemsbooked=Bookings.objects.filter(status="Not Delivered").order_by('-applydate', 'applytime')
    return render(request, "adminpannelapp/AllorderedItems.html", {'items': itemsbooked})


def usersdelete(request,ram):
    us = UsersData.objects.get(id=ram)
    User.objects.get(id=us.user.id).delete()
    return redirect("Allusers")

def Feedbackreviews(request):
    reviews=Contact.objects.all()
    return render(request, "adminpannelapp/Feedbackreviews.html",{'reviews':reviews})