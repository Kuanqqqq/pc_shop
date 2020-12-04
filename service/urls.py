# from django.contrib.staticfiles.urls import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from .views import *
 
'''This file is all about generate the url link'''

urlpatterns = [
    path('regiester_order/<int:pk>/',regiester_order,name='regiester_order'),         #http://127.0.0.1:8000/products/checkout/1/
    ]