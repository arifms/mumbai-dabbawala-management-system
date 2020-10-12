from django.contrib import admin
from .models import canteenItems,orders,customer,cart

# Register your models here.
admin.site.register(canteenItems)
admin.site.register(customer)
admin.site.register(orders)
admin.site.register(cart)