# # from django.urls import path, include
# # from django.contrib.auth.views import LoginView
# # from . import views

# # urlpatterns = [
# #     path('about/', views.about_view, name="SIEMS_about"),
# #     path('', views.home , name="SIEMS_home"),
# #     path('cars/', views.cars, name="SIEMS_cars"),
# #     path('importer/', views.importer_home, name='importer_home'),
# #     path('exporter/', views.exporter_home, name='exporter_home'),
# #     # path('login/', LoginView.as_view(template_name='core/cars.html'), name='login'),
# #     path('administrator/', views.administrator_home, name='administrator_home'),
# #     path('finance_manager/', views.finance_manager_home, name='finance_manager_home'),
# #     path('compliance_officer/', views.compliance_officer_home, name='compliance_officer_home'),
# #     path('car_store_manager/', views.car_store_manager_home, name='car_store_manager_home'),
# #     path('coffee_store_manager/', views.coffee_store_manager_home, name='coffee_store_manager_home'),
# #     path('accounts/login/', views.login_user, name='login1'),  # Keep this one
# #     path('accounts/', include('django.contrib.auth.urls')),
# # ]

# from django.urls import path, include
# from django.contrib.auth.views import LoginView
# from . import views
# from orders.views import *


# urlpatterns = [
#     path('about/', views.about_view, name="SIEMS_about"),
#     path('contacts/', views.contact , name = "contact"),
#     path('', views.home, name="SIEMS_home"),
#     path('cars/', views.cars, name="SIEMS_cars"),
#     path('orders/', views.orders, name="SIEMS_orders"),
#     path('submit_order/', include("orders.urls"), name='submit_order'), 
#     path('importer/', views.importer_home, name='importer_home'),
#     path('importer/imports/', views.imports, name='importer_home'),
#     path('finance_manager/financeSell/confirm', views.confirm_buy, name='confirm_buy'),
#     path('administrator/', views.administrator_home, name='administrator_home'),
#     path('finance_manager/', views.finance_manager_home, name='finance_manager_home'),
#     path('finance_manager/financeAvailable', views.finance_available, name='finance_available'),
#     path('finance_manager/financeImport', views.get_import, name='finance_import'),
#     path('finance_manager/financeSell', views.get_buy, name='finance_sell'),
#     path('compliance_officer/', views.compliance_officer_home, name='compliance_officer_home'),
#     path('car_store_manager/', views.car_store_manager_home, name='car_store_manager_home'),
#     path('coffee_store_manager/', views.coffee_store_manager_home, name='coffee_store_manager_home'),
#     path('shipments/', views.shipments_home, name='shipments'),
#     path('finance_manager/financeImport/confirm', views.confirm_order, name='confirm_order'),
#     ]
from django.urls import path, include
from . import views

urlpatterns = [
    path('about/', views.about_view, name="SIEMS_about"),
    path('contacts/', views.contact, name="contact"),
    path('', views.home, name="SIEMS_home"),
    path('cars/', views.cars, name="SIEMS_cars"),
    path('orders/', views.orders, name="SIEMS_orders"),
    path('submit_order/', include("orders.urls"), name='submit_order'), 
    path('importer/', views.importer_home, name='importer_home'),
    path('importer/imports/', views.imports, name='importer_home'),
    path('finance_manager/financeSell/confirm', views.confirm_buy, name='confirm_buy'),
    path('administrator/', views.administrator_home, name='administrator_home'),
    path('finance_manager/', views.finance_manager_home, name='finance_manager_home'),
    path('finance_manager/financeAvailable', views.get_avail, name='finance_available'),
    path('finance_manager/financeImport', views.get_import, name='finance_import'),
    path('finance_manager/financeSell', views.get_buy, name='finance_sell'),
    path('compliance_officer/', views.compliance_officer_home, name='compliance_officer_home'),
    # path('car_store_manager/', views.car_store_manager_home, name='car_store_manager_home'),
    path('car_store_manager/', views.get_orders, name='get_order'),
    # path('coffee_store_manager/', views.coffee_store_manager_home, name='coffee_store_manager_home'),
    path('shipments/', views.shipments_home, name='shipments'),
    path('finance_manager/financeImport/confirm', views.confirm_order, name='confirm_order'),
    path('finance_manager/financeSell/confirm', views.confirm_buy, name='confirm_buy'),
    path('car_store_manager/confirm', views.imp_store, name='imp_store'),
    path('car_store_manager/confirms', views.sell_store, name='sell_store'),
    

]
