from django.urls import path
from . import views

urlpatterns =[
    path("index",views.adminpannelindex,name="adminpannelindex"),
    path("login",views.adminpannellogin,name="adminpannellogin"),
    path("Allitemsadmin",views.Allitemsadmin,name="Allitemsadmin"),
    path("AllNotDeliveredItems",views.AllNotDeliveredItems,name="AllNotDeliveredItems"),
    path("AllDeliveredItems",views.AllDeliveredItems,name="AllDeliveredItems"),
    path("AllCanceledItems",views.AllCanceledItems,name="AllCanceledItems"),
    path("AllSuppliers",views.AllSuppliers,name="AllSuppliers"),
    path("Allusers",views.Allusers,name="Allusers"),
    path("AllRejectedSuppliers",views.AllRejectedSuppliers,name="AllRejectedSuppliers"),
    path("AllPendingSuppliers",views.AllPendingSuppliers,name="AllPendingSuppliers"),
    path("AllAcceptedSuppliers",views.AllAcceptedSuppliers,name="AllAcceptedSuppliers"),
    path("Suppliersstatus/<int:ram>",views.Suppliersstatus,name="Suppliersstatus"),
    path("Suppliersdelete/<int:ram>",views.Suppliersdelete,name="Suppliersdelete"),
    path("usersdelete/<int:ram>",views.usersdelete,name="usersdelete"),
    path("adminlogout",views.adminlogout,name="adminlogout"),
    path("Feedbackreviews",views.Feedbackreviews,name="Feedbackreviews"),
]