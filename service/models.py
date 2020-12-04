from django.db import models
from client.models import Customer
from product.models import *

# Create your models here.
class Purchase (models.Model):
	customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
	cpu = models.ForeignKey(Cpu,null=True,blank=True,on_delete=models.CASCADE)
	motherboard = models.ForeignKey(Motherboard,null=True,blank=True,on_delete=models.CASCADE)
	cpu_quantity = models.IntegerField()
	motherboard_quantity=models.IntegerField()

	#product.append(cpu)
	#product.append(motherboard)
	#for i in product:
	#	print (i)


	#monitor = models.ForeignKey(Product, null=True,on_delete=models.CASCADE)
	
	#price = models.IntegerField()
	
	#total_spend = models.CharField(max_length=200)

	'''def quantity():
		q=input("Quantity")
		return q==models.CharField(max_length=200)

	def price():
		p=input()
		return p'''

	def total_spend(self):
		t = (self.cpu.price if self.cpu else 0) *self.cpu_quantity + (self.motherboard.price if self.motherboard else 0) * self.motherboard_quantity #if self.motherboard_quantity else 0) 
		return t

	def __str__(self):
		return self.customer.__str__()


class Order(models.Model):
	product=models.ForeignKey(Cpu,on_delete=models.CASCADE)
	price=models.FloatField()
	qty=models.IntegerField()
	register_dt=models.DateTimeField()
	#customer_firstname=models.ForeignKey()
	#customer_lastname=models.ForeignKey()
	#customer_phonenumber=models.ForeignKey()

	#
	def __str__(self):
		return  self.product.__str__()
