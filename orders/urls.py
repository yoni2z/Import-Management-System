# orders/urls.py
from django.urls import path
from . import views
from core.templates import *


urlpatterns = [
    path('', views.purchase, name='submit_order'),  # Example URL pattern
    # path('importers/', views.imports, name='importer_home'),
    # Other URL patterns for the 'orders' app
]
