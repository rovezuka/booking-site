from django.contrib import admin

# Register your models here.
from .models import Item, Reservation

# Register your models here.

admin.site.register(Item)
admin.site.register(Reservation)