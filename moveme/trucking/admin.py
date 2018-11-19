from django.contrib import admin

from .models import Order, Driver, Vehicle


admin.site.register(Order)
admin.site.register(Driver)
admin.site.register(Vehicle)

# Register your models here.
