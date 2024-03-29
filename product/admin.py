from django.contrib import admin

# Register your models here.

from .models import Socket, Cpu, Cpu_cooler, Motherboard, Memory, Gpu, Power_supply, Build


class CpuAdmin(admin.ModelAdmin):
	list_display = ['name', 'price']


class CoolerAdmin(admin.ModelAdmin):
	list_display = ['name', 'price']


class MotherboardAdmin(admin.ModelAdmin):
	list_display = ['name', 'price']


class MemoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'price']


class GpuAdmin(admin.ModelAdmin):
	list_display = ['name', 'price']


class PowerAdmin(admin.ModelAdmin):
	list_display = ['name', 'price']


class BuildAdmin(admin.ModelAdmin):
	list_display = ['user_token', 'cpu', 'cooler',
	                'motherboard', 'memory', 'gpu',
	                'power', 'total_spend']
	list_filter = ['cpu', 'gpu']


admin.site.register(Socket)
admin.site.register(Cpu, CpuAdmin)
admin.site.register(Cpu_cooler, CoolerAdmin)
admin.site.register(Motherboard, MotherboardAdmin)
admin.site.register(Memory, MemoryAdmin)
admin.site.register(Gpu, GpuAdmin)
admin.site.register(Power_supply, PowerAdmin)
admin.site.register(Build, BuildAdmin)
