from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from storeapp.models import Suppliers

from userapp.models import UsersData

from adminapp.models import Contact


def index(request):
    return render(request,"index.html")

def loginall(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        userss = authenticate(username=username, password=password)
        if userss is not None:
            if userss.is_superuser:
                login(request, userss)
                return redirect('adminpannelindex')
        if userss is not None:
            try:
                user1 = Suppliers.objects.get(user=userss)
                if user1.type == "Supplier" and user1.status == "Accepted":
                    login(request, userss)
                    return render(request, 'storeapp/Supplierhome.html', {"status": "Login Completed"})
                else:
                    return render(request, 'login.html', {"status": "Not Accepted"})
            except:
                user1 = UsersData.objects.get(user=userss)
                if user1.type == "user":
                    login(request, userss)
                    return redirect('userhome')
        else:
            return render(request, 'login.html', {"status": "User Not Found"})
    return render(request,"login.html")

def signupall(request):
    return render(request,"signup.html")

def ContactForm(request):
    if request.method=="POST":
        user=request.POST['user']
        mail = request.POST['mail']
        phone = request.POST['phone']
        rating = request.POST['rating']
        problem = request.POST['problem']
        address = request.POST['address']
        Contact(user=user,mail=mail,phone=phone,rating=rating,problem=problem,address=address).save()
        return redirect("index")
    return render(request,"contact.html")