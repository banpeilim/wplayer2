from django.urls import path
from . import views


urlpatterns = [
    path('flight-data/', views.getFlights, name="routes"),
    path('data-page/', views.data_page, name="data_page"),
    path('send-signal/', views.send_signal, name="send_signal"),
    path('inventory-data/', views.getInventory, name="inventory_data"),


]