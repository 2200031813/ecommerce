from django.shortcuts import render, redirect
from app.models import Category,Product

from django.contrib.auth import authenticate,login
from app.models import UserCreateForm
#from app.models import,FeedbackForm

from django.contrib.auth.decorators import login_required
from cart.cart import Cart
def Master(request):
    return render(request, "master.html")

def Index(request):
    category = Category.objects.all()  # Retrieve all categories from the Category model

    categoryID = request.GET.get('category')
    if categoryID:
        product = Product.objects.filter(sub_category = categoryID).order_by('-id')
    else:
        product = Product.objects.all()
    context = {
        'category': category,
        'product':product,
    }
    return render(request, "index.html", context)

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password1 = form.cleaned_data['password1'],
            )
            # login(request,new_user)
            return redirect('index')
    else:
        form = UserCreateForm()

    context = {
        'form':form,
    }
    return render(request,'registration/signup.html',context)

@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('index')


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect('cart_detail')


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('cart_detail')


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect('cart_detail')


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail')


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')


def Contact_Page(request):
    return render(request,'contact-us.html')


#def feedback(request):
    #if request.method == 'POST':
       # form = FeedbackForm(request.POST)
       # if form.is_valid():
            #form.save()
            #return redirect('index')  # Redirect to the index page or wherever you want
    #else:
        #form = FeedbackForm()

    #context = {'form': form}
    #return render(request, 'feedback.html', context)
def feedback(request):
    return render(request,'feedback.html')
def logout(request):
    request.session.clear()
    return redirect('master')