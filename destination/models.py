from django.db import models
from adminstrations.models import Cars_Model

class Inventory(models.Model):
    
    Model = models.ForeignKey(Cars_Model,on_delete=models.CASCADE)
    Color = models.CharField(max_length=50, default='Unspecified')
    Count = models.IntegerField(default=0)



# Create your models here.
