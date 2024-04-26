from django.urls import path
from . import views

urlpatterns = [
    path("index",views.Supplierhome,name="Supplierindex"),
    path("Suppliersignup",views.Suppliersignup,name="Suppliersignup"),
    path("Supplierlogin",views.Supplierlogin,name="Supplierlogin"),
    path("Additems",views.Additems,name="Additems"),
    path("Allitems",views.Allitems,name="Allitems"),
    path("Deleteitems/<int:pk>/",views.Deleteitems,name="Deleteitems"),
    path("Ordereditems",views.Ordereditems,name="Ordereditems"),
    path("Delivereditems",views.Delivereditems,name="Delivereditems"),
    path("Canceleditems",views.Canceleditems,name="Canceleditems"),
    path("updatestatus/<int:ram>",views.updatestatus,name="updatestatus"),
    path("Edititems/<int:pk>/",views.Edititems,name="Edititems"),
    path("logoutSupplier",views.logoutSupplier,name="logoutSupplier"),
]