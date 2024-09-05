from django.db import models

from orders.models import importOrder, Buy
from adminstrations.models import *

# Create your models here.
class Order(models.Model):
    id = models.IntegerField(primary_key=True,unique=True,blank=True)   
    TrackingNo = models.ForeignKey(importOrder, on_delete=models.CASCADE,unique=True)
    Model = models.ForeignKey(Cars_Model, on_delete=models.CASCADE)
class Sell(models.Model):
    id = models.IntegerField(primary_key=True,unique=True,blank=True)   
    OrderNo = models.ForeignKey(Buy, on_delete=models.CASCADE,unique=True)
    Model = models.ForeignKey(Cars_Model, on_delete=models.CASCADE)

    
 
class FinancialTransaction(models.Model):
    TRANSACTION_TYPES = (
        ('payment', 'Payment'),
        ('refund', 'Refund'),
        ('fee', 'Fee'),
        ('tax', 'Tax'),
    )
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
class TaxRecord(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='tax_records')
    tax_type = models.CharField(max_length=50)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tax_date = models.DateField()
