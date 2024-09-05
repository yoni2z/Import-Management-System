from django.contrib import admin
from .models import *


# admin.site.register(Order)
# admin.site.register(Document)
# admin.site.register(Shipment)
admin.site.register(Buy)
admin.site.register(importOrder)


# Register your models here.
# python manage.py migrate <your_app_name> zero
# python manage.py migrate --fake-initial
