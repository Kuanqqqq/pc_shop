from django.shortcuts import render, redirect
from service.models import OrderItems
from client.models import Customer
from product.models import Cpu, Build, Cpu_cooler, Motherboard, Memory, Gpu, Power_supply
import datetime
import string
import secrets
alphabet = string.ascii_letters + string.digits

from django.contrib.contenttypes.models import ContentType

# Create your views here.
# def order(request):
#     if request.method.POST:
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             .field=form.cleaned
#     return

#def shopping_cart(request):
#   token = request.GET.get('token')
#    return render(request, 'checkout.html')


def regiester_order(request, prod_name, pk):
    #-------------------------------------------------------------
    #
    #-------------------------------------------------------------
    qty = request.POST.get('qty')
    #print('Product pk: ', pk, ' Quantity: ', qty)
    #print('prod_name innnnnnnnnnnnnn: ',prod_name)
    product_class = eval(prod_name)
    #print('product_class: ' ,product_class)
    product = product_class.objects.get(pk=pk)
    #print('product: ', product)
    price = product.price
    #print('price: ',price)

    total_price = float(qty)*float(price)
    #print('total_price: ', total_price)

    order_item = OrderItems()
    order_item.sold_product = product_class.objects.get(pk=pk)
    order_item.buyer = Customer.objects.last()#need further develop
    order_item.date_ordered = datetime.datetime.now()
    order_item.qty = qty
    order_item.sold_price = price
    order_item.content_type = ContentType.objects.get(product)
    print('order_item.content_type: ',order_item.content_type)
    order_item.object_id = pk
    order_item.save()

    #orderitem = order.content_type()

    #product_type = eval(prod_name)  # eg: <class 'product.models.Cpu'> 
    #product = product_type.objects.get(pk=pk)
    # eg: AMD Ryzen 5 3600

    #product.stock -= 1
    #product.save()

    '''print('in regiester_order')
    print(request.POST)
    cpu = Cpu.objects.get(pk=pk)
    new_order = Order(
        #Order() in models.py; define all the variable
        product = cpu,
        price = cpu.price,
        qty = request.POST.get('qty'),
        register_dt = datetime.datetime.now()
        )
'''
    return render(request,'Congratulations.html') 
    