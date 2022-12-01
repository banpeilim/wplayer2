from django.contrib import admin
from .models import Flight
from .models import Inventory

# Register your models here.

admin.site.register(Flight)
admin.site.register(Inventory)