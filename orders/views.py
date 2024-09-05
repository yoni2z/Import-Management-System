from django.shortcuts import render
from django.http import HttpResponse
from orders.models import *
import random
from core.models import User

def generate_random_integer():
    return random.randint(100000, 999999)
def generate_random_integer1():
    return random.randint(100000, 999999)
def generate_random_integer2():
    return random.randint(1, 10000)



def purchase(request):
    if request.method == 'POST':
        model = request.POST['model']
        # year = request.POST['year']
        # price = request.POST['price']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        color = request.POST['color']
        date = request.POST['delivery_date']
        orderNo = generate_random_integer1()
        try:
            car_model = Cars_Model.objects.get(Model=model)
        except Cars_Model.DoesNotExist:
            return HttpResponse(f"Car model '{model}' does not exist.")

        my = Buy(
                 OrderNo = orderNo,
                 Model= car_model,
                #  Year=year,
                #  Price=price,
                 Name=name,
                 Email=email,
                 PhoneNumber=phone,
                 Location=address,
                 Color=color,
                 Date=date,
                 )
        my.save()
        return HttpResponse("Order Saved Successfully")
    else:
        return render(request,"core/orders.html") 
 
