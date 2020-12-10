from django.db import models
from django.contrib import messages
from django.core.exceptions import ValidationError
from monitor.models import Product


# Create your models here.
class Socket(models.Model):
	socket = models.CharField(max_length=10)

	def __str__(self):
		return self.socket


class Cpu(models.Model):
	name = models.CharField(max_length=200)
	voltage = models.FloatField()
	price = models.FloatField()
	socket = models.ForeignKey(Socket, null=True, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='image', blank=True)
	stock = models.PositiveIntegerField (null=True, blank=True)

	def __str__(self):
		return self.name


class Cpu_cooler(models.Model):
	name = models.CharField(max_length=200)
	voltage = models.FloatField()
	price = models.FloatField()
	socket = models.ManyToManyField(Socket, blank=True)
	image = models.ImageField(upload_to='image', blank=True)
	stock = models.PositiveIntegerField (null=True, blank=True)

	def __str__(self):
		return self.name + 'Soket: (' + ', '.join(self.socket.values_list('socket', flat=True)) + ')'


class Motherboard(models.Model):
	name = models.CharField(max_length=200)
	voltage = models.FloatField()
	price = models.FloatField()
	socket = models.ForeignKey(Socket, null=True, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='image', blank=True)
	stock = models.PositiveIntegerField (null=True, blank=True)

	def __str__(self):
		return self.name


class Memory(models.Model):
	name = models.CharField(max_length=200)
	voltage = models.CharField(max_length=200)
	price = models.FloatField()
	image = models.ImageField(upload_to='image', blank=True)
	stock = models.PositiveIntegerField (null=True, blank=True)

	def __str__(self):
		return self.name


class Gpu(models.Model):
	name = models.CharField(max_length=200)
	voltage = models.FloatField()
	price = models.FloatField()
	image = models.ImageField(upload_to='image', blank=True)
	stock = models.PositiveIntegerField (null=True, blank=True)

	def __str__(self):
		return self.name


class Power_supply(models.Model):
	name = models.CharField(max_length=200)
	voltage = models.FloatField()
	price = models.FloatField()
	image = models.ImageField(upload_to='image', blank=True)
	stock = models.PositiveIntegerField (null=True, blank=True)

	def __str__(self):
		return self.name


class Build(models.Model):
	user_token = models.CharField(null=True, max_length=10)
	cpu = models.ForeignKey(Cpu, null=True, on_delete=models.CASCADE)
	cooler = models.ForeignKey(Cpu_cooler, null=True, on_delete=models.CASCADE)
	motherboard = models.ForeignKey(Motherboard, null=True, on_delete=models.CASCADE)
	memory = models.ForeignKey(Memory, null=True, on_delete=models.CASCADE)
	gpu = models.ForeignKey(Gpu, null=True, blank=True, on_delete=models.CASCADE)
	power = models.ForeignKey(Power_supply, null=True, on_delete=models.CASCADE)
	#monitor = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)

	def voltage_validator(self):
		total_voltage = self.cpu.voltage + self.cooler.voltage + self.motherboard.voltage + (self.gpu.voltage if self.gpu else 0)
		return self.power.voltage > total_voltage

	def total_spend(self):
		self.total_spend = (self.cpu.price if self.cpu else 0) + (self.cooler.price if self.cooler else 0)+(self.motherboard.price if self.motherboard else 0)+(self.memory.price if self.memory else 0)+(self.gpu.price if self.gpu else 0)+(self.power.price if self.power else 0)
		return self.total_spend

	def clean(self):
		if not self.voltage_validator():
			raise ValidationError('Need Bigger Power Supply')
		if self.cpu.socket != self.motherboard.socket:
			raise ValidationError('Incompatble Socket')

	def socket_lst(self):
		socket_lst = Socket.objects.all()
		if self.cooler:
			socket_lst = socket_lst.filter(id__in=[socket.id for socket in self.cooler.socket.all()])
		if self.motherboard:
			# socket_lst = socket_lst.filter(socket=self.motherboard.socket.socket)
			socket_lst = socket_lst.filter(id__in=[self.motherboard.socket.id])
		if self.cpu:
			socket_lst = socket_lst.filter(id__in=[self.cpu.socket.id])

		print('socket_lst', socket_lst)
		return socket_lst

	# def save(self, *args, **kwargs):
	# 	print('Voltage results: ', self.voltage_validator())
	# 	super(Build, self).save(*args, **kwargs)

	# def __str__(self):
	# 	return  self.voltage_validator().__str__()
