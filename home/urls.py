from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("" , views.index , name='home'),
    path("contact" , views.contact , name='contact'),
    path("booking" , views.booking , name='booking'),
    path("booked" , views.booked , name='booked'),
    path("avilable" , views.avilable , name='avilable'),
    path("booked1" , views.booked1 , name='booked1')

]