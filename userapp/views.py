from datetime import datetime, date

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import UsersData, Cart, Bookings, Payment
from storeapp.models import Items
from storeapp.models import Suppliers

categories = ["Electronics", "Fashion",  "Appliances",
                  "Books and Media", "Beauty", "Sports and Fitness",
                  "Baby", "Automotive", "Grocery and Food",
                  "Pets", "Home Improvement", "Office Supplies", "Travel and Luggage"
                  ]
catego=["OVEN",]
# Create your views here.
def userhome(request):
    return render(request,"userapp/userindex.html")



def usersignup(request):
    if (request.method == "POST"):
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
            return render(request, 'userapp/usersignup.html', {"status": "Mail already exists"})
        if confirm_password == password:
            newuser = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username,
                                               password=password)
            newagent = UsersData.objects.create(user=newuser, phone=phno, address=address, image=image,
                                             type="user")
            newuser.save()
            newagent.save()
            return redirect('userhome')
        else:
            return render(request, 'userapp/usersignup.html', {"status": "Passwords are Not Same"})
    return render(request,"userapp/usersignup.html")




def userlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        userss = authenticate(username=username, password=password)
        if userss is not None:
            user1 = UsersData.objects.get(user=userss)
            if user1.type == "user":
                login(request, userss)
                return redirect('userhome')
                # return render(request, 'userapp/userindex.html', {"status": "Login Completed"})
        else:
            return render(request, 'userapp/usersignup.html', {"status": "User Not Found"})
    return render(request, 'userapp/userlogin.html')

def userlogout(request):
    logout(request)
    return redirect('index')

def useritems(request):
    if not request.user.is_authenticated:
        return redirect("loginall")
    items=Items.objects.all()
    clit = UsersData.objects.get(user=request.user)
    cartfood = Cart.objects.filter(bookinguser=clit)
    data = []
    for i in cartfood:
        data.append(i.item.id)
    context = {
        'items': items,
        'data': data,
        'categories':categories
    }
    return render(request, 'userapp/useritems.html', context)

def cart(request,ram):
    if not request.user.is_authenticated:
        return redirect("loginall")
    items = Items.objects.get(id=ram)
    items.itemstockquantity-=1
    items.save();
    user = UsersData.objects.get(user=request.user)
    Cart(supplier=items.supplier,item=items,bookinguser=user,quantity=1).save()
    return redirect("useritems")

def cartdata(request):
    if not request.user.is_authenticated:
        return redirect("loginall")
    us=UsersData.objects.get(user=request.user)
    cart = Cart.objects.filter(bookinguser=us).order_by('id')
    total_cost = sum(item.item.itemprice * item.quantity for item in cart)
    total_items = sum(item.quantity for item in cart)
    context = {
        'items': cart,
        'total_cost': total_cost,
        'total_items': total_items,
    }
    return render(request,"userapp/usercart.html",context)

def removecart(request,ram):
    if not request.user.is_authenticated:
        return redirect("loginall")
    cart = Cart.objects.get(id=ram)
    items = Items.objects.get(itemname=cart.item)
    items.itemstockquantity += cart.quantity
    items.save();
    cart.delete()
    return redirect("cartdata")



def update_quantity(request, item_id,ram):
    if not request.user.is_authenticated:
        return redirect("loginall")
    if request.method == 'POST':
        # print("ram",ram)
        quantity = int(request.POST.get('quantity'))
        cart_item = Cart.objects.get(id=item_id)
        items = Items.objects.get(itemname=cart_item.item)
        if(ram==1 and items.itemstockquantity>0):
            items.itemstockquantity -= 1
            cart_item.quantity = quantity
        elif ram==5:
            items.itemstockquantity += 1
            cart_item.quantity = quantity
        items.save();
        cart_item.save()
        return JsonResponse({'message': 'Quantity updated successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)

def itemcategory(request,strcat):
    if not request.user.is_authenticated:
        return redirect("loginall")
    items = Items.objects.filter(itemcategary=strcat)
    clit = UsersData.objects.get(user=request.user)
    cartfood = Cart.objects.filter(bookinguser=clit)
    data = []
    for i in cartfood:
        data.append(i.item.id)
    context = {
        'items': items,
        'data': data,
        'categories':categories
    }
    return render(request, 'userapp/useritems.html', context)
def itemcat(request,strca):
    if not request.user.is_authenticated:
        return redirect("loginall")
    items = Items.objects.filter(itemname=strca)
    clit = UsersData.objects.get(user=request.user)
    cartfood = Cart.objects.filter(bookinguser=clit)
    data = []
    for i in cartfood:
        data.append(i.item.id)
    context = {
        'items': items,
        'data': data,
        'categories':categories
    }
    return render(request, 'userapp/useritems.html', context)



def bookall(request):
    if not request.user.is_authenticated:
        return redirect("loginall")
    clit = UsersData.objects.get(user=request.user)
    cartfood = Cart.objects.filter(bookinguser=clit)
    # total_cost = sum(item.item.itemprice * item.quantity for item in cart)
    # total_items = sum(item.quantity for item in cart)
    for foods in cartfood:
        newBook = Bookings(supplier=foods.item.supplier, item=foods.item, bookinguser=clit, quantity=foods.quantity, applydate=date.today(),
                           applytime=datetime.now().time(), status="Not Delivered")
        newBook.save()
    cartfood.delete()
    return redirect("Notdelivered")

def Notdelivered(request):
    if not request.user.is_authenticated:
        return redirect("loginall")
    clit = UsersData.objects.get(user=request.user)
    booked = Bookings.objects.filter(status="Not Delivered",bookinguser=clit).order_by('-applydate', 'applytime')
    return render(request, 'userapp/todeliver.html', {'items': booked})

def Delivered(request):
    if not request.user.is_authenticated:
        return redirect("loginall")
    clit = UsersData.objects.get(user=request.user)
    booked = Bookings.objects.filter(status="Delivered",bookinguser=clit).order_by('-applydate', 'applytime')
    return render(request, 'userapp/todeliver.html', {'items': booked})


def Canceled(request):
    if not request.user.is_authenticated:
        return redirect("loginall")
    clit = UsersData.objects.get(user=request.user)
    booked = Bookings.objects.filter(status="Canceled",bookinguser=clit).order_by('-applydate', 'applytime')
    return render(request, 'userapp/todeliver.html', {'items': booked})

def Cancelitem(request,ram):
    if not request.user.is_authenticated:
        return redirect("loginall")
    booked = Bookings.objects.get(id=ram)
    booked.status="Canceled"
    booked.save()
    return redirect("Notdelivered")

def Deleteitem(request,ram):
    if not request.user.is_authenticated:
        return redirect("loginall")
    booked = Bookings.objects.get(id=ram)
    booked.delete()
    return redirect("Canceled")


from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def changepassword(request):
    if not request.user.is_authenticated:
        return redirect("loginall")
    if request.method == "POST":
        password = request.POST['password']
        newpassword1 = request.POST['newpassword1']
        newpassword2 = request.POST['newpassword2']
        user = UsersData.objects.get(user=request.user)
        vvr = User.objects.get(id=user.user.id)
        if vvr.check_password(password):
            if newpassword1==newpassword2:
                new_password_hash = make_password(newpassword1)
                vvr.password = new_password_hash
                vvr.save()
                return render(request, "userapp/changepassword.html",{'status':"Password Updated sucess"})
            else:
                return render(request, "userapp/changepassword.html",{'status':"Both passwords are not same"})
        else:
            return render(request, "userapp/changepassword.html", {'status': "old password is wrong"})
    return render(request, "userapp/changepassword.html")


import razorpay
@csrf_exempt
def paymentforitems(request):
    client=razorpay.Client(auth=("rzp_test_WwBCla7kD4lfGX", "rsmiBqvgC3Xj5oIh5eBs3bhG"))
    user = UsersData.objects.get(user=request.user)
    cart = Cart.objects.filter(bookinguser=user).order_by('id')
    total_cost = sum(item.item.itemprice * item.quantity for item in cart)
    total_items = sum(item.quantity for item in cart)
    number_as_float = float(total_cost)
    amount = int(number_as_float) * 100
    response_payment=client.order.create(dict(
            amount= amount,
            currency= "INR"
    ))
    # print(response_payment)
    order_id=response_payment['id']
    order_status=response_payment['status']

    if order_status=="created":
        Payment(bookinguser=user,amount=amount,order_id=order_id).save()
        response_payment['name']="ram"
        context = {
            'items': cart,
            'total_cost': total_cost,
            'total_items': total_items,
            'payment': response_payment
        }
        return render(request, "userapp/userpaymentpage.html", context)
    return redirect("cartdata")




@csrf_exempt
def paymentstatus(request):
     response1 = request.POST
     params_dict = {
        "razorpay_payment_id": response1["razorpay_payment_id"],
        "razorpay_order_id": response1["razorpay_order_id"],
        "razorpay_signature": response1["razorpay_signature"]
     }
     # create razorpay client
     client=razorpay.Client(auth=("rzp_test_WwBCla7kD4lfGX", "rsmiBqvgC3Xj5oIh5eBs3bhG"))

     try:
         status = client.utility.verify_payment_signature(params_dict)
         coldcoffee = Payment.objects.get(order_id = response1['razorpay_order_id'])
         coldcoffee.razorpay_payment_id = response1['razorpay_payment_id']
         coldcoffee.paid = True
         coldcoffee.save()
         return redirect("bookall")
     except:
         return HttpResponse("Not Paid")