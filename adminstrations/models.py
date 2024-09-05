from django.db import models


class Supplier(models.Model):
    SUPPLIER = (
        ('hyundai', 'HYUNDAI'),
        ('honda', 'HONDA'),
        ('toyota', 'TOYOTA'),
        ('volkswagen', 'VOLKSWAGEN'),
    )
    COUNTRY = (
        ('japan', 'JAPAN'),
        ('germany', 'GERMANY'),
        ('southkorea', 'SOUTH KOREA'),
        
    )
    SID = models.PositiveIntegerField(primary_key=True,unique=True)
    supp_name = models.CharField(max_length=20, choices=SUPPLIER)
    country = models.CharField(max_length=255,choices=COUNTRY)
    phone = models.PositiveIntegerField()
    email = models.EmailField(unique=True, null=True, blank=True )
class Cars_Model(models.Model):
    CAR_TYPES = (
        ('bz4x','BZ4X'),
        ('id6','ID6'),
        ('tucson','TUCSON'),
        ('tucson-hybrid','TUCSON HYBRID'),
        ('honda-e','HONDA E'),
    )
    SPEC = (
        ('fuel','FUEL'),
        ('electric','ELECTRIC'),
    )
    Model = models.CharField(primary_key=True,max_length=20, unique=True, choices=CAR_TYPES)
    Specifications = models.CharField(max_length=20,choices=SPEC)
    Price = models.PositiveIntegerField()
    Year = models.CharField(max_length=4, default='2023')
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE)
