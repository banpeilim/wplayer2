from signal import signal
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .models import Flight, Inventory
from .serializers import FlightSerializer, InventorySerializer
from django.db.models import F
from django.views.generic import TemplateView
import socket


# Create your views here.

@api_view(['GET'])
def getFlights(request):

    flights = Flight.objects.order_by('?')
    serializers = FlightSerializer(flights, many=True)
    return Response(serializers.data)




def data_page(request):

    inventory = Inventory.objects.all()

    latest_out_of_stock = Inventory.objects.filter(signal=False).filter(stock=0)


    for x in latest_out_of_stock:
        UDP_IP = x.udpip
        UDP_PORT = 55555
        MESSAGE = "2"
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
        x.signal = True
        x.save()

    context ={
        "inventory": inventory,
        }
    return render(request, 'data-page.html', context)



def send_signal(request):

    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        display = Inventory.objects.get(id=post_id)
        UDP_IP = display.udpip
        UDP_PORT = 55555
        MESSAGE = "2"
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
        display.signal = True
        display.save()

    context ={
        "inventory": "inventory",
        }
    return render(request, 'data-page.html', context)




@api_view(['GET'])
def getInventory(request):

    inventory = Inventory.objects.all()
    serializers = InventorySerializer(inventory, many=True)
    return Response(serializers.data)
