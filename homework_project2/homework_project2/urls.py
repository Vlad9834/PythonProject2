"""
URL configuration for homework_project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from homeproject2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index ),
    path("Phone shop/",views.store,name="shop"),
    path("add-phone/",views.add_phone,name="add_phone"),
    path("our-contacts/",views.contacts,name="contacts"),
    path("phone/<int:phone_id>",views.show_products,name="show_products"),
]
