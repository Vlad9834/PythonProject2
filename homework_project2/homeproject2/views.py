from django.db.models import Q, Count
from django.http import HttpRequest
from django.shortcuts import render

from homeproject2.models import TelephoneModel, Brand

from homeproject2.models import Case

# from homeproject2.models import Brand

menu = [
    {"url": "shop", "name": "каталог"},
    {"url": "add_phone", "name": "Добавить телефон"},
    {"url": "contacts", "name": "контакты"},
]


def index(request):
    context = {
        "menu": menu,
    }
    return render(request, "homeproject2/index.html", context=context)


def store(request):
    brands = Brand.objects.all()
    # brands = (Brand.objects.annotate(total=Count("phones"),filter=Q(phones__is_active=1))).filter(total__gt=0).distinct("name")
    phones = TelephoneModel.objects.all()
    context = {
        "phones": phones,
        "brands": brands,
        "menu": menu,
    }
    return render(request, "homeproject2/store.html", context=context)

def show_phones_by_brand(request,brand_id):
    phones = TelephoneModel.objects.filter(brand=brand_id).filter(is_active=1)
    context = {
        "menu":menu,
        "phones":phones,
    }
    return render(request,"homeproject2/show_phones_by_brand.html",context=context)



def show_products(request, phone_id):
    phone = TelephoneModel.objects.get(id=phone_id)
    context = {
        "phone": phone,
        "menu": menu,
    }
    return render(request, "homeproject2/show_products.html", context=context)


def add_phone(request):
    context = {
        "menu": menu
    }
    return render(request, "homeproject2/add_phone.html", context=context)


def contacts(request):
    context = {
        "menu": menu
    }
    return render(request, "homeproject2/contacts.html", context=context)

def cases(request):
    case = Case.objects.all()
    context = {
        "menu":menu,
        "case":case,
    }
    return render(request,"homeproject2/cases.html",context=context)

def show_phone(request,phone_id):
    phone = TelephoneModel.objects.get(id=phone_id)
    cases = Case.objects.filter(cases=phone)
    context = {
        "phone":phone,
        "menu":menu,
        "cases":cases,
    }
    return render(request,"homeproject2/show_phone.html",context=context)
