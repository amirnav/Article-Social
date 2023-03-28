from django.urls import path
from . import views

urlpatterns=[
    path("orders",views.add_enquiry,name="order"),
]