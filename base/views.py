from signal import signal
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .models import Flight, Inventory, Doctor
from .serializers import FlightSerializer, InventorySerializer, DoctorSerializer
from django.db.models import F
from django.views.generic import TemplateView
import socket


# Create your views here.

@api_view(['GET'])
def getFlights(request):

    flights = Flight.objects.order_by('?')
    serializers = FlightSerializer(flights, many=True)
    return Response(serializers.data)





@api_view(['GET'])
def getInventory(request):

    inventory = Inventory.objects.all()
    serializers = InventorySerializer(inventory, many=True)
    return Response(serializers.data)



@api_view(['GET'])
def getDoctors(request):

    doctors = Doctor.objects.all()
    serializers = DoctorSerializer(doctors, many=True)
    return Response(serializers.data)