         
import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from orders.views import generate_random_integer
from core.models import User
from core.backends import CustomUserBackend
from orders.models import *
from adminstrations.models import *
from django.urls import reverse
from finance.models import *
from django.contrib import messages
from destination.models import Inventory

def home(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        try:
            testUser = User.objects.get(username=name)
            if testUser.password == password:
                if testUser.user_type == "importer":
                    return redirect('importer_home')
                elif testUser.user_type == "store_keeper":
                    return redirect('get_order')
                elif testUser.user_type == "finance_manager":
                    return redirect('finance_manager_home')
                else:
                    return HttpResponse("User type not recognized.")
            else:
                return HttpResponse("Incorrect Password")
        except User.DoesNotExist:
            return HttpResponse(f"User with username '{name}' does not exist.")
    else:
        return render(request, 'core/home.html')

def about_view(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def cars(request):
    return render(request, 'core/cars.html')

def orders(request):
    return render(request, 'core/orders.html')

# @login_required
def importer_home(request):
    return render(request, 'core/importer_home.html')

@login_required
def exporter_home(request):
    return render(request, 'core/exporter_home.html')

@login_required
def administrator_home(request):
    return render(request, 'core/administrator_home.html')

@login_required
def finance_manager_home(request):
    return render(request, 'core/finance_manager_home.html')

def finance_available(request):
    return render(request, 'core/financeAvailable.html')

def finance_import(request):
    return render(request, 'core/financeImport.html')

def finance_sell(request):
    return render(request, 'core/financeSell.html')

@login_required
def compliance_officer_home(request):
    return render(request, 'core/compliance_officer_home.html')

@login_required
def car_store_manager_home(request): 
    imp_orders = Order.objects.select_related('TrackingNo', 'Model').all() 
    sell_orders = Sell.objects.select_related('OrderNo', 'Model').all() 
    in_INV =  Inventory.objects.select_related('Model').all() 
    return render(request, 'core/car_store_manager_home.html', {'imp_orders': imp_orders, 'sell_orders': sell_orders,'in_INV':in_INV})

@login_required
def coffee_store_manager_home(request):
    return render(request, 'core/coffee_store_manager_home.html')

@login_required
def shipments_home(request):
    return render(request, 'core/shipment.html')

def imports(request):
    if request.method == 'POST':
        name = request.POST['name']
        model = request.POST['carModel']
        color = request.POST['color']
        date = request.POST['orderDate']
        count = request.POST['count']
        trackingno = generate_random_integer()
        try:
            user = User.objects.get(username=name)
        except User.DoesNotExist:
            return HttpResponse(f"User with username '{name}' does not exist.")
        try:
            car_model = Cars_Model.objects.get(Model=model)
        except Cars_Model.DoesNotExist:
            return HttpResponse(f"Car model '{model}' does not exist.")

        my = importOrder(
            TrackingNo=trackingno,
            Name=user,
            Model=car_model,
            Color=color,
            Date=date,
            Count=count,
        )
        my.save()
        return HttpResponse("Import Order Saved Successfully")
    else:
        return render(request, "core/importer_home.html")

def get_import(request):
    import_orders = importOrder.objects.select_related('Model').all()
    return render(request, 'core/financeImport.html', {'import_orders': import_orders})

def get_avail(request):
    avail = Inventory.objects.select_related('Model').all()
    return render(request, 'core/financeAvailable.html', {'avail': avail})



def get_buy(request):
    buy_orders = Buy.objects.select_related('Model').all()
    return render(request, 'core/financeSell.html', {'buy_orders': buy_orders})

def get_orders(request):
    imp_orders = Order.objects.select_related('Model').all()
    sell_orders = Sell.objects.select_related('Model').all()
    inv_table = Inventory.objects.select_related('Model').all()
    return render(request, 'core/car_store_manager_home.html', {'imp_orders': imp_orders,'sell_orders': sell_orders,'inv_table':inv_table})
 
     
def confirm_buy(request):
    if request.method == 'POST':
        try:
            order = int(request.POST['order'])
            orders = Buy.objects.get(OrderNo=order)
            ids = generate_random_integer2()
            my = Sell(
                id=ids,
                OrderNo=orders,
                Model=orders.Model,
            )
            my.save()
            return HttpResponse("Buy Order Confirmed Successfully")
        except Buy.DoesNotExist:
            return HttpResponse("Error: Buy order does not exist.")
        except Cars_Model.DoesNotExist:
            return HttpResponse("Error: Cars model does not exist.")
        except Exception as e:
            return HttpResponse(f"Error confirming buy: {str(e)}")
    else:
        return render(request, "core/financeSell.html")



def generate_random_integer2():
    return random.randint(1, 10000)

def confirm_order(request):
    if request.method == 'POST':
        try:
            track = request.POST['track']
            tracks = importOrder.objects.get(TrackingNo=track)
            ids = generate_random_integer2()
            my = Order(
                id=ids,
                TrackingNo=tracks,
                Model=tracks.Model,
            )
            my.save()
            return HttpResponse("Import Order Confirmed Successfully")
        except importOrder.DoesNotExist:
            return HttpResponse("Error: Import order does not exist.")
        except Cars_Model.DoesNotExist:
            return HttpResponse("Error: Cars model does not exist.")
        except Exception as e:
            return HttpResponse(f"Error confirming order: {str(e)}")
    else:
        return render(request, "core/financeImport.html")
    
def imp_store(request):
    if request.method == 'POST':
        try:
            model = request.POST['model']
            track = int(request.POST['track'])
            models = Cars_Model.objects.get(Model=model)
            order = importOrder.objects.get(TrackingNo=track)
            counts = int(order.Count)
            try:
                my = Inventory.objects.get(Model=models,Color=order.Color)
                my.Count += counts
            
            except:
                my = Inventory(
                Model=models,
                Color= order.Color,
                Count=counts,)
            my.save()
            return HttpResponse("Added to Store Successfully")
        except importOrder.DoesNotExist:
            return HttpResponse("Error: No Import Order exist.")
        except Cars_Model.DoesNotExist:
            return HttpResponse("Error: Cars model does not exist.")
        except Exception as e:
            return HttpResponse(f"Error adding order to store: {str(e)}")
        
    else:
        return render(request,"core/car_store_manager_home.html")
def sell_store(request):
    if request.method == 'POST':
        try:
            model = request.POST['model']
            order = int(request.POST['order'])
            models = Cars_Model.objects.get(Model=model)
            order = Buy.objects.get(OrderNo=order)
            my = Inventory.objects.get(Model=models,Color=order.Color)
            if my.Count >= 1:
                my.Count -= 1 
                my.save()           
                return HttpResponse("Car Purchased Successfully")
            else:
                return HttpResponse("Not Enough car in Inventory")
        except Buy.DoesNotExist:
            return HttpResponse("Error: No Purchasing Order exist.")
        except Cars_Model.DoesNotExist:
            return HttpResponse("Error: Cars model does not exist.")
        except Inventory.DoesNotExist:
            return HttpResponse("Error: There is no such car in inventory.")
        
        except Exception as e:
            return HttpResponse(f"Car Already Purchased: {str(e)}")
        
    else:
        return render(request,"core/car_store_manager_home.html")
    
