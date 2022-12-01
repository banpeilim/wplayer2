from rest_framework import serializers
from .models import Flight, Inventory

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['time', 'destination', 'flight', 'gate', 'status']



class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['storeid', 'productid', 'udpip', 'stock', 'signal']