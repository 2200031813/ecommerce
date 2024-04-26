from django.urls import path
from . import views

urlpatterns = [
    path("index",views.userhome,name="userhome"),
    path("usersignup",views.usersignup,name="usersignup"),
    path("userlogin",views.userlogin,name="userlogin"),
    path("items",views.useritems,name="useritems"),
    path("cart/<int:ram>",views.cart,name="cart"),
    path("removecart/<int:ram>",views.removecart,name="removecart"),
    path("cartdata",views.cartdata,name="cartdata"),
    path("bookall",views.bookall,name="bookall"),
    path("Notdelivered",views.Notdelivered,name="Notdelivered"),
    path("Delivered",views.Delivered,name="Delivered"),
    path("Canceled",views.Canceled,name="Canceled"),
    path("Cancelitem/<int:ram>",views.Cancelitem,name="Cancelitem"),
    path("Deleteitem/<int:ram>",views.Deleteitem,name="Deleteitem"),
    path("userlogout",views.userlogout,name="userlogout"),
    path('update_quantity/<int:item_id>/<int:ram>/', views.update_quantity, name='update_quantity'),
    path('itemcategory/<str:strcat>/', views.itemcategory, name='itemcategory'),
    path('itemcat/<str:strca>/', views.itemcat, name='itemcat'),

    path('changepassword', views.changepassword, name='changepassword'),
    path('paymentforitems', views.paymentforitems, name='paymentforitems'),
    path("payment-status",views.paymentstatus,name='payment-status')
]