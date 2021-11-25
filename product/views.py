from django.shortcuts import render, redirect
from product.models import Cpu, Build, Cpu_cooler, Motherboard, Memory, Gpu, Power_supply
from monitor.models import Product
import string
import secrets
alphabet = string.ascii_letters + string.digits


def main_page(request):
    #----------------------------------------------------------------------------------------------------------
    # Get token from url, if there is a token and only one, the function will add a token into the 
    # build object. Otherwise, the function will generate a length 10 token with letters and digits,
    # then save the token inside of the build object. In the end, the function will return render main_page.html file
    # and config.
    #----------------------------------------------------------------------------------------------------------

    # print('The request META ', request)
    # <QueryDict: {'token': ['RbVmGCkSQI']}>
    token = request.GET.get('token')
    print(token)  # RbVmGCkSQI

    if token and len(Build.objects.filter(user_token=token)):
        config = Build.objects.get(user_token=token)  # Build object (63)
    else:
        config = Build()
        config.user_token = ''.join(secrets.choice(alphabet) for i in range(10))
        # generate a length 10 code with letters and digits
        config.save()

    return render(request, 'main_page.html', {'config': config})


def get_product_lst(request, prod_name):  # token as a parameter
    #---------------------------------------------------------------------------------------------------------
    # prod_name is a parameter from main_page.html, name of parameters must be inheritance from models.py 
    # The function will get the token from url, and use the token could find the specific build in the build model. 
    # Using eval() to evaluate the specific model, then use hasattr() to check if the specified object has the 
    # specified attribute. If there is, show the filtered obejct. If there is not, show everything in the object.
    # In the end, the function will return render product_list.html with product_lst, token, and prod_name. 
    #---------------------------------------------------------------------------------------------------------

    #print("prod_name, ",prod_name)
    token = request.GET.get('token')
    build = Build.objects.get(user_token=token)
    product_type = eval(prod_name)
    
    #print("product_type, ", product_type)
    # eg: <class 'product.models.Cpu'>
    # <class 'product.models.Cpu'>

    socket_lst = build.socket_lst()
    if hasattr(product_type, 'socket') and socket_lst:
       product_lst = product_type.objects.filter(socket__in=socket_lst, stock__gt=0)
    else:
       product_lst = product_type.objects.filter(stock__gt=0)
       #stock_gt=0 means stock greater than 0

    return render(request, 'product_list.html', {'product_lst': product_lst, 'token': token, 'prod_name': prod_name})


def add_product(request, prod_name, pk):
    #-----------------------------------------------------------------------------------------------------------
    # prod_name is a parameter to identify the product model.(must be exact as class name in the models.py)
    # pk is a parameter to identify the product by its ID. 
    # The function will get the specific product object according to the ID and add/update them in the build object. 
    #-----------------------------------------------------------------------------------------------------------

    token = request.GET.get('token')
    product_type = eval(prod_name)
    # eg: AMD Ryzen 5 3600

    product = product_type.objects.get(pk=pk)
    print("product, ",product)
    # cpu = Cpu.objects.get(pk=pk)
    build = Build.objects.get(user_token=token)
    if prod_name == 'Cpu':
       build.cpu = product

    elif prod_name == 'Cpu_cooler':
       build.cooler = product

    elif prod_name == 'Motherboard':
       build.motherboard = product

    elif prod_name == 'Memory':
       build.memory = product

    elif prod_name == 'Gpu':
       build.gpu = product

    elif prod_name == 'Power_supply':
       build.power = product

    elif prod_name == 'Product':
       build.monitor = product

    build.save()
    return redirect('/?token=' + build.user_token)


def cpu_details(request, pkk):
    my_cpu = Cpu.objects.get(pk=pkk)
    return render(request, 'cpu_details.html', {'my_cpu': my_cpu})  # 'cpu_detail.html' is the link to html


def cpu_image(request, num):
    my_cpu = Cpu.objects.get(pk=num)
    return render(request, 'cpu_image.html', {'my_cpu': my_cpu})


def checkout(request, prod_name, pk):
    print('prod_name: ', prod_name) #Gpu

    product_type = eval(prod_name) 
    print('product_type: ', product_type) #<class 'product.models.Gpu'>

    product = product_type.objects.get(pk=pk)
    print('product: ', product) #EVGA GeForce RTX 2060 SUPER 8 GB SC ULTRA

    return render(request, 'checkout.html', {'prod_name': prod_name, 'product': product})


def del_product(request, prod_name):

    #-----------------------------------------------------------------------------------------------------------
    # prod_name is a parameter to identify the product model (must be exact as class name in the models.py).
    # The function will find the specific build object accoring to the token and update them as None in the build object.
    #-----------------------------------------------------------------------------------------------------------
    
    token = request.GET.get('token')
    # product_type = eval(prod_name)
    # print("product_type, ", product_type)
    # product = product_type.objects.get(pk=pk)
    # print("product, ",product)
    # cpu = Cpu.objects.get(pk=pk)

    build = Build.objects.get(user_token=token)

    product_type = eval(prod_name)
    

    if prod_name == 'Cpu':
       build.cpu = None

    elif prod_name == 'Cpu_cooler':
       build.cooler = None

    elif prod_name == 'Motherboard':
       build.motherboard = None

    elif prod_name == 'Memory':
       build.memory = None

    elif prod_name == 'Gpu':
       build.gpu = None

    elif prod_name == 'Power_supply':
       build.power = None

    elif prod_name == 'Product':
       build.monitor = None

    build.save()
    return redirect('/?token=' + build.user_token)


def stock_check(request, prod_name, pk):

    #------------------------------------------------------------------------------------------------------
    #
    #
    #
    #------------------------------------------------------------------------------------------------------

    token = request.GET.get('token')
    build = Build.objects.get(user_token=token)
    product_type = eval(prod_name)
    product = product_type.objects.get(pk=pk)

    return



'''def all_cpu(request): # token as a parameter
    token = request.GET.get('token')
    build = Build.objects.get(user_token=token)
    build.cpu = None
    socket_lst = build.socket_lst()
    if socket_lst:
       cpu_lst = Cpu.objects.filter(socket__in=socket_lst)
    else:
       cpu_lst = Cpu.objects.all()
    add_product_url_name = 'add_cpu'
    
    return render(request,'product_list.html', 
       {
       'product_lst': cpu_lst, 
       'token': token,
       'add_product_url_name':add_product_url_name
       })


def all_cpu_cooler(request):
    token = request.GET.get('token')
    build = Build.objects.get(user_token=token)
    build.cooler = None
    socket_lst = build.socket_lst()
    if socket_lst:
       cpu_cooler_lst = Cpu_cooler.objects.filter(socket__in=socket_lst).distinct()
    else:
       cpu_cooler_lst = Cpu_cooler.objects.all()
    add_product_url_name = 'add_cooler'
    
    return render(request,'product_list.html', 
       {
       'product_lst': cpu_cooler_lst,
       'token': token, 
       'add_product_url_name':add_product_url_name
       })

def all_motherboard(request):
    token = request.GET.get('token')
    build = Build.objects.get(user_token=token)
    build.motherboard = None
    socket_lst = build.socket_lst()
    if socket_lst:
       motherboard_lst = Motherboard.objects.filter(socket__in=socket_lst)
    else:
       motherboard_lst = Motherboard.objects.all()
    add_product_url_name = 'add_motherboard'
    return render(request,'product_list.html', 
       {
       'product_lst': motherboard_lst,
       'token':token,
       'add_product_url_name':add_product_url_name
       })


def all_memory(request):
    token = request.GET.get('token')
    memory_lst = Memory.objects.all()
    add_product_url_name = 'add_memory'
    return render(request,'product_list.html', 
       {
       'product_lst': memory_lst,
       'token':token,
       'add_product_url_name':add_product_url_name
       })

def all_gpu(request):
    token = request.GET.get('token')
    gpu_lst = Gpu.objects.all()
    add_product_url_name = 'add_gpu'
    return render(request,'product_list.html', 
       {
       'product_lst': gpu_lst,
       'token':token,
       'add_product_url_name':add_product_url_name
       })

def all_powersupply(request):
    token = request.GET.get('token')
    powersupply_lst = Power_supply.objects.all()
    add_product_url_name = 'add_power'
    return render(request,'product_list.html', 
       {
       'product_lst': powersupply_lst,
       'token':token,
       'add_product_url_name':add_product_url_name
       })

def all_monitor(request):
    token = request.GET.get('token')
    monitor_lst = Product.objects.all()
    add_product_url_name = 'add_monitor'
    return render(request,'product_list.html', 
       {
       'product_lst': monitor_lst,
       'token':token,
       'add_product_url_name':add_product_url_name
       })


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
    return redirect('/?token=' +build.user_token)'''