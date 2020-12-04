from django.contrib import admin

# Register your models here.
from .models import Brand, Size, Resolution,Product,CPU



class ProductAdmin(admin.ModelAdmin):
	list_display = ['product_code','brand','size','resolution_str', 'resolution_k','price']
	list_filter = ['brand','size']


admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Resolution)
admin.site.register(Product,ProductAdmin)
admin.site.register(CPU)
