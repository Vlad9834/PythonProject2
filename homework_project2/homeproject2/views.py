from django.http import HttpRequest
from django.shortcuts import render

from homeproject2.models import TelephoneModel


menu = [
    {"url":"shop","name":"каталог"},
    {"url":"add_phone","name":"Добавить телефон"},
    {"url":"contacts","name":"контакты"},



]

def index(request):
    context={
        "menu":menu,
    }
    return render(request,"homeproject2/index.html",context=context)

def store(request):
    phones = TelephoneModel.objects.all()
    context = {
     "phones":phones,
        "menu": menu,
        }
    return render(request,"homeproject2/store.html",context=context)

def show_products(request,phone_id):
    phone = TelephoneModel.objects.get(id = phone_id)
    context = {
        "phone":phone,
        "menu": menu,
    }
    return render(request,"homeproject2/show_products.html",context=context)


def add_phone(request):
    context = {
        "menu":menu
    }
    return render(request,"homeproject2/add_phone.html",context=context)

def contacts(request):
    context = {
        "menu":menu
    }
    return render(request,"homeproject2/contacts.html",context=context)

