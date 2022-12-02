from django.contrib import admin
from .models import Flight
from .models import Inventory
from .models import Doctor
from .models import Coffee

# Register your models here.

admin.site.register(Flight)
admin.site.register(Inventory)
admin.site.register(Doctor)
admin.site.register(Coffee)