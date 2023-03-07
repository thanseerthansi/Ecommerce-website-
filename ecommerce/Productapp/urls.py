"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from .views import *


urlpatterns = [
    path('category/',CategoryView.as_view()),
    path('image/',ImageView.as_view()),
    path('product/',ProductView.as_view()),
    path('status/',PurchaseStatusView.as_view()),
    path('city/',CityView.as_view()),
    path('order/',OrderView.as_view()),
    # path('ordererproduct/',Orderedproductview.as_view()),
    path('contact/',ContactView.as_view()),
    path('missingorder/',MissingOrderView.as_view()),
    path('metatags/',MetatagsView.as_view()),
    # path('missingorderproduct/',Missingorderedproductview.as_view()),
    
  
]
