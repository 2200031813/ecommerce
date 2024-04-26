from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Suppliers, Items
from userapp.models import Bookings
categories = ["Electronics", "Fashion and Apparel", "Home and Furniture", "Appliances",
                  "Books and Media", "Beauty and Personal Care", "Sports and Fitness",
                  "Baby and Kids", "Automotive", "Health and Wellness", "Grocery and Food",
                  "Pets", "Home Improvement", "Office Supplies", "Travel and Luggage"
                  ]

# Create your views here.
def Supplierhome(request):
    if not request.user.is_authenticated:
        return redirect("loginall")
    return render(request,'storeapp/Supplierhome.html')

def Suppliersignup(request):
    if(request.method=="POST"):
        lastname = request.POST['lastname']
        firstname = request.POST['firstname']
        phno = request.POST['phno']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        address = request.POST['address']
        image = request.FILES.get('image', None)
        vc = User.objects.filter(email=email).count()
        if vc == 1:
            return render(request, 'storeapp/Suppliersignup.html', {"status": "Mail already exists"})

        if confirm_password==password:
            newuser = User.objects.create_user(first_name=firstname,last_name=lastname, email=email, username=username, password=password)
            newagent = Suppliers.objects.create(user=newuser, phone=phno, address=address, image=image,
                                                    type="Supplier", status="pending")
            newuser.save()
            newagent.save()
            return render(request, 'storeapp/Supplierhome.html',{"status":"Registration Completed"})
        else:
            return render(request, 'storeapp/Suppliersignup.html',{"status":"Passwords are Not Same"})
    return render(request,'storeapp/Suppliersignup.html')


def Supplierlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        userss = authenticate(username=username, password=password)
        if userss is not None:
            user1 = Suppliers.objects.get(user=userss)
            if user1.type == "Supplier" and user1.status=="Accepted":
                login(request, userss)
                return render(request, 'storeapp/Supplierhome.html', {"status": "Login Completed"})
            else:
                return render(request, 'storeapp/Supplierlogin.html', {"status": "Not Accepted"})
        else:
            return render(request, 'storeapp/Suppliersignup.html', {"status": "User Not Found"})
    return render(request, 'storeapp/Supplierlogin.html')

def logoutSupplier(request):
    logout(request)
    return redirect('index')

def Additems(request):
    if not request.user.is_authenticated:
        return redirect("loginall")

    if request.method=="POST":
        itemname=request.POST['itemname']
        itemprice=request.POST['itemprice']
        itemcategary=request.POST['itemcategary']
        itemdescription=request.POST['itemdescription']
        itemstockquantity=request.POST['itemstockquantity']
        itemrating=4
        itemimage = request.FILES.get('image', None)
        Supplier = Suppliers.objects.get(user=request.user)
        Items(supplier=Supplier,itemname=itemname,itemprice=itemprice,itemimage=itemimage,itemcategary=itemcategary,itemdescription=itemdescription,itemrating=itemrating,itemstockquantity=itemstockquantity).save()
        return render(request, "storeapp/Additems.html",{"status":"Item Added Success fully"})
    return render(request,"storeapp/Additems.html",{'categories':categories})

def Allitems(request):
    if not request.user.is_authenticated:
        return redirect("loginall")
    Supplier = Suppliers.objects.get(user=request.user)
    items=Items.objects.filter(supplier=Supplier)
    return render(request, "storeapp/Allitems.html",{"items":items})

def Deleteitems(request,pk):
    if not request.user.is_authenticated:
        return redirect("loginall")
    Items.objects.get(id=pk).delete()
    return redirect("Allitems")

def Edititems(request,pk):
    if not request.user.is_authenticated:
        return redirect("loginall")
    item=Items.objects.get(id=pk)
    if request.method =="POST":
        item.itemname = request.POST['itemname']
        item.itemprice = request.POST['itemprice']
        item.itemcategary = request.POST['itemcategary']
        item.itemdescription = request.POST['itemdescription']
        item.itemstockquantity = request.POST['itemstockquantity']
        item.itemrating = 4
        item.save();
        return redirect("Allitems")
    return render(request,"storeapp/Edititems.html",{'item':item,'categories':categories})



def Ordereditems(request):
    if not request.user.is_authenticated:
        return redirect("loginall")
    supplier = Suppliers.objects.get(user=request.user)
    itemsbooked=Bookings.objects.filter(supplier=supplier,status="Not Delivered").order_by('-applydate', 'applytime')
    return render(request, "storeapp/Ordereditems.html", {'items': itemsbooked})


def Delivereditems(request):
    if not request.user.is_authenticated:
        return redirect("loginall")
    supplier = Suppliers.objects.get(user=request.user)
    itemsbooked=Bookings.objects.filter(supplier=supplier,status="Delivered").order_by('-applydate', 'applytime')
    return render(request, "storeapp/Ordereditems.html", {'items': itemsbooked})

def Canceleditems(request):
    if not request.user.is_authenticated:
        return redirect("loginall")
    supplier = Suppliers.objects.get(user=request.user)
    itemsbooked=Bookings.objects.filter(supplier=supplier,status="Canceled").order_by('-applydate', 'applytime')
    return render(request, "storeapp/Ordereditems.html", {'items': itemsbooked})

def updatestatus(request,ram):
    if not request.user.is_authenticated:
        return redirect("loginall")
    booked = Bookings.objects.get(id=ram)
    booked.status = "Delivered"
    booked.save()
    return redirect("Ordereditems")