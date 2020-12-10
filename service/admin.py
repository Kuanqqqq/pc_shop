from django.contrib import admin

# Register your models here.
from .models import OrderItems

class OrderItemsAdmin(admin.ModelAdmin):
	list_display = ['content_object', 'qty', 'sold_price']
	list_filter =['buyer', 'date_ordered', 'sold_product']

admin.site.register(OrderItems, OrderItemsAdmin)
#admin.site.register(Order)