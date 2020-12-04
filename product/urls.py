# from django.contrib.staticfiles.urls import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from .views import *
 
'''This file is all about generate the url link'''

urlpatterns = [
    path('cpu_details/<int:pkk>/', cpu_details, name='cpu_details'),  #http://127.0.0.1:8000/products/product/1/
    path('cpu_img/<int:num>/', cpu_image, name='cpu_image'),  #http://127.0.0.1:8000/products/product_img/2/
    path('checkout/<int:num>/',checkout,name='checkout'),         #http://127.0.0.1:8000/products/checkout/1/
   
    path('cpu/<str:token>/',all_cpu,name='all_cpu'),  #token in the url
    path('del_cpu/', del_cpu, name='del_cpu'),

    path('cooler/<str:token>/',all_cpu_cooler,name='all_cpu_cooler'),
    path('del_cooler',del_cooler,name='del_cooler'),

    path('motherboard/<str:token>/',all_motherboard,name='all_motherboard'),
    path('del_motherboard',del_motherboard,name='del_motherboard'),

    path('memory/<str:token>/',all_memory,name='all_memory'),
    path('del_memory',del_memory,name='del_memory'),

    path('gpu/<str:token>/',all_gpu,name='all_gpu'),
    path('del_gpu',del_gpu,name='del_gpu'),

    path('powersupply/<str:token>/',all_powersupply,name='all_powersupply'),
    path('del_power',del_power,name='del_power'),

    path('monitor/<str:token>/',all_monitor,name='all_monitor'),
    path('del_monitor',del_monitor,name='del_monitor'),

    path('add_cpu/<int:pkk>/',add_cpu,name='add_cpu'),

    path('add_cooler/<int:pkk>/',add_cooler,name='add_cooler'),
    path('add_motherboard/<int:pkk>/',add_motherboard,name='add_motherboard'),
    path('add_memory/<int:pkk>/',add_memory,name='add_memory'),
    path('add_gpu/<int:pkk>/',add_gpu,name='add_gpu'),
    path('add_power/<int:pkk>/',add_power,name='add_power'),
    path('add_monitor/<int:pkk>/',add_monitor,name='add_monitor'),
    ]