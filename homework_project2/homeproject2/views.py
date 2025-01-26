from django.shortcuts import render

from homeproject2.models import TelephoneModel


# Create your views here.

def index(request):
    return render(request,"homeproject2/index.html")

def store(request):
    phones = TelephoneModel.objects.all()
    context = {
     "phones":phones,
    }
    return render(request,"homeproject2/store.html",context=context)

def show_products(request,phone_id):
    phone = TelephoneModel.objects.get(id = phone_id)
    context = {
        "phone":phone
    }
    return render(request,"homeproject2/show_products.html",context=context)


