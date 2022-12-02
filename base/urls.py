from django.urls import path
from . import views


urlpatterns = [
    path('flight-data/', views.getFlights, name="routes"),
    path('inventory-data/', views.getInventory, name="inventory_data"),
    path('doctor-data/', views.getDoctors, name="doctor_data"),
    path('coffee-data/', views.getCoffee, name="coffee_data"),


]