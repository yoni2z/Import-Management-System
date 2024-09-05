from django.contrib import admin


from .models import *

admin.site.register(FinancialTransaction)
admin.site.register(TaxRecord)
admin.site.register(Sell)

# admin.site.register(Order)
# admin.py


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'TrackingNo', 'Model']  # Add other fields as needed
    # Add more configurations as needed

# Register your models here.
