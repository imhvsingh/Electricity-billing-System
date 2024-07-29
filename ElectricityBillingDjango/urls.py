"""ElectricityBillingDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from electricity.views import *
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index'),
    path('admin_login', admin_login,name='admin_login'),
    path('admin_home', admin_home,name='admin_home'),
    path('add_Customer', add_Customer,name='add_Customer'),
    path('view_Customer', view_Customer,name='view_Customer'),
    path('edit_Customer/<int:pid>', edit_Customer, name='edit_Customer'),
    path('delete_Customer/<int:pid>', delete_Customer, name='delete_Customer'),
    path('add_Connection', add_Connection,name='add_Connection'),
    path('view_Connection', view_Connection,name='view_Connection'),
path('edit_Connection/<int:pid>', edit_Connection, name='edit_Connection'),
    path('delete_Connection/<int:pid>', delete_Connection, name='delete_Connection'),
    path('add_Bill', add_Bill,name='add_Bill'),
    path('view_Bill', view_Bill,name='view_Bill'),
    path('delete_Bill/<int:pid>', delete_Bill, name='delete_Bill'),
    path('change_password', change_password, name='change_password'),
    path('logout', Logout, name='logout'),
    path('payment/<int:pid>', payment, name='payment'),
    path('viewmybill',viewmybill,name='viewmybill'),
    path('about/', about,name='about'),

]
