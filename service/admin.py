from django.contrib import admin

# Register your models here.
from .models import Purchase,Order

class PurchaseAdmin(admin.ModelAdmin):
	list_display = ['customer','cpu','cpu_quantity','motherboard','motherboard_quantity','total_spend']

admin.site.register(Purchase,PurchaseAdmin)
admin.site.register(Order)