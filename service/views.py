from django.shortcuts import render, redirect, HttpResponseRedirect
#from django.contrib.auth.forms import 
from product.models import Cpu
from service.models import Order
import datetime

# Create your views here.
# def order(request):
# 	if request.method.POST:
# 		form = OrderForm(request.POST)
# 		if form.is_valid():
# 			.field=form.cleaned
# 	return

def regiester_order(request, pk):
	print('in regiester_order')
	print(request.POST)
	cpu = Cpu.objects.get(pk=pk)
	new_order = Order(
		#Order() in models.py; define all the variable
		product = cpu,
		price = cpu.price,
		qty = request.POST.get('qty'),
		register_dt = datetime.datetime.now()
		)
	new_order.save()
	# return HttpResponseRedirect(request.META.get('HHT_REFERER'))
	return redirect('cpu_details', pkk=pk)  #cpu_details in views.py, 