from django.shortcuts import render, redirect
from product.models import Cpu, Build,Cpu_cooler,Motherboard,Memory,Gpu,Power_supply
from monitor.models import Product
import string
import secrets
alphabet = string.ascii_letters + string.digits


def main_page(request):
	# token = None
	
	#print('The request META ', request) #<QueryDict: {'token': ['RbVmGCkSQI']}>
	token = request.GET.get('token')
	print(token) #RbVmGCkSQI
	if token and len(Build.objects.filter(user_token=token)):
		print(len(Build.objects.filter(user_token=token))) #1
		config = Build.objects.get(user_token=token)#Build object (63)
		print(config)
	else:
		config = Build()
		config.user_token = ''.join(secrets.choice(alphabet) for i in range(10)) 
		#generate a length 10 code with letters and digits
		config.save()

	return render(request,'main_page.html',{'config':config})

def all_cpu(request, token): # token as a parameter
	build = Build.objects.get(user_token=token)
	build.cpu = None
	socket_lst = build.socket_lst()
	if socket_lst:
		cpu_lst = Cpu.objects.filter(socket__in=socket_lst)
	else:
		cpu_lst = Cpu.objects.all()
	
	return render(request,'cpu_list.html', {'cpu_lst': cpu_lst, 'token': token})

'''def all_cpu(request):
	token=request.GET.get('token')
	cpu_lst=Cpu.objects.all()
'''

def all_cpu_cooler(request,token):
	build = Build.objects.get(user_token=token)
	build.cooler = None
	socket_lst = build.socket_lst()
	if socket_lst:
		cpu_cooler_lst = Cpu_cooler.objects.filter(socket__in=socket_lst).distinct()
	else:
		cpu_cooler_lst = Cpu_cooler.objects.all()
	
	return render(request,'cooler_list.html', {'cpu_cooler_lst': cpu_cooler_lst,'token': token})

def all_motherboard(request,token):
	build = Build.objects.get(user_token=token)
	build.motherboard = None
	socket_lst = build.socket_lst()
	if socket_lst:
		motherboard_lst = Motherboard.objects.filter(socket__in=socket_lst)
	else:
		motherboard_lst = Motherboard.objects.all()
	return render(request,'motherboard_lst.html', {'motherboard_lst': motherboard_lst,'token':token})

def all_memory(request,token):
	memory_lst = Memory.objects.all()
	return render(request,'memory_lst.html', {'memory_lst': memory_lst,'token':token})

def all_gpu(request,token):
	gpu_lst = Gpu.objects.all()
	return render(request,'gpu_list.html', {'gpu_lst': gpu_lst,'token':token})

def all_powersupply(request,token):
	powersupply_lst = Power_supply.objects.all()
	return render(request,'powersupply_lst.html', {'powersupply_lst': powersupply_lst,'token':token})

def all_monitor(request,token):
	monitor_lst = Product.objects.all()
	return render(request,'monitor_lst.html', {'monitor_lst': monitor_lst,'token':token})

def cpu_details(request, pkk):
	my_cpu = Cpu.objects.get(pk=pkk)
	return render(request,'cpu_details.html', {'my_cpu': my_cpu}) #'cpu_detail.html' is the link to html


def cpu_image(request,num): 
	my_cpu = Cpu.objects.get(pk=num)
	return render(request,'cpu_image.html', {'my_cpu': my_cpu})

'''def cooler_image(request,num):
	my_cooler = Cpu_cooler.objects.get(pk=num)
	return '''

def checkout(request,num):
	my_cpu = Cpu.objects.get(pk=num)
	return render(request,'checkout.html',{'my_cpu':my_cpu})

def del_cpu(request): #set token as a variable then using .GET.get('token')
	print('Request.GET', request.GET)
	token=request.GET.get('token')
	#cpu = Cpu.objects.get(pk=pkk)
	print('Token', token)
	build = Build.objects.get(user_token=token)
	print('Build', build)
	build.cpu = None
	build.save()
	return redirect('/?token=' + build.user_token)

def del_cooler(request):
	token=request.GET.get('token')
	build = Build.objects.get(user_token=token)
	build.cooler = None
	build.save()
	return redirect('/?token=' + build.user_token)

def del_motherboard(request):
	token=request.GET.get('token')
	build = Build.objects.get(user_token=token)
	build.motherboard=None
	build.save()
	return redirect('/?token=' + build.user_token)

def del_memory(request):
	token=request.GET.get('token')
	build = Build.objects.get(user_token=token)
	build.memory = None
	build.save()
	return redirect('/?token=' + build.user_token)

def del_gpu(request):
	token=request.GET.get('token')
	build = Build.objects.get(user_token=token)
	build.gpu = None
	build.save()
	return redirect('/?token=' + build.user_token)

def del_power(request):
	token=request.GET.get('token')
	build = Build.objects.get(user_token=token)
	build.power = None
	build.save()
	return redirect('/?token=' + build.user_token)

def del_monitor(request):
	token=request.GET.get('token')
	build = Build.objects.get(user_token=token)
	build.monitor = None
	build.save()
	return redirect('/?token=' + build.user_token)

def add_cpu(request,pkk):
	token = request.GET.get('token')
	cpu = Cpu.objects.get(pk=pkk)
	build = Build.objects.get(user_token=token)
	build.cpu= cpu
	build.save()
	return redirect('/?token=' + build.user_token)

def add_cooler(request,pkk):
	token = request.GET.get('token')
	cooler = Cpu_cooler.objects.get(pk=pkk)
	build = Build.objects.get(user_token=token)
	build.cooler= cooler
	build.save()
	return redirect('/?token=' + build.user_token)

def add_motherboard(request,pkk):
	token = request.GET.get('token')
	motherboard = Motherboard.objects.get(pk=pkk)
	build = Build.objects.get(user_token=token)
	build.motherboard= motherboard
	build.save()
	return redirect('/?token=' +build.user_token)

def add_memory(request,pkk):
	token = request.GET.get('token')
	memory = Memory.objects.get(pk=pkk)
	build = Build.objects.get(user_token=token)
	build.memory= memory
	build.save()
	return redirect('/?token=' +build.user_token)

def add_gpu(request,pkk):
	token = request.GET.get('token')
	gpu = Gpu.objects.get(pk=pkk)
	build = Build.objects.get(user_token=token)
	build.gpu= gpu
	build.save()
	return redirect('/?token=' +build.user_token)

def add_power(request,pkk):
	token = request.GET.get('token')
	power = Power_supply.objects.get(pk=pkk)
	build = Build.objects.get(user_token=token)
	build.power = power
	build.save()
	return redirect('/?token=' +build.user_token)

def add_monitor(request,pkk):
	token = request.GET.get('token')
	monitor = Product.objects.get(pk=pkk)
	build = Build.objects.get(user_token=token)
	build.monitor= monitor
	build.save()
	return redirect('/?token=' +build.user_token)