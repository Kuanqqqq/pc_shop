from django.db import models
from django.contrib.contenttypes.models import ContentType
from client.models import Customer
from product.models import *
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

#class Order(models.Model):
#	user = models.CharField(max_length = 20)
#	total_sum = models.FloatField()
#	register_dt=models.DateTimeField()
#	ordered_dt=models.DateTimeField(null=True, blank=True)


	#customer_firstname=models.ForeignKey()
	#customer_lastname=models.ForeignKey()
	#customer_phonenumber=models.ForeignKey()

	#
#	def __str__(self):
#		return self.user

class OrderItems(models.Model):
	#order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
	content_type = models.ForeignKey(ContentType, null=True, blank=True, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField(null=True, blank=True)
	content_object = GenericForeignKey('content_type', 'object_id')
	sold_product = models.CharField(null=True, blank=True, max_length=100)
	qty = models.PositiveIntegerField(null=True, blank=True)
	sold_price = models.FloatField(null=True, blank=True)
	buyer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
	date_ordered = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.content_object.__str__()
