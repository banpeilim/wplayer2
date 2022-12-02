from rest_framework import serializers
from .models import Flight, Inventory, Doctor, Coffee

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['time', 'destination', 'flight', 'gate', 'status']


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['storeid', 'productid', 'udpip', 'stock', 'signal']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['department', 'name', 'university']


class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = ['name', 'price', 'stock']