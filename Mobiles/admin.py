from django.contrib import admin
from .models import Payment, Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','category','data', 'price', 'stock')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name','email','number','address','city','state','zip')


admin.site.register(Product, ProductAdmin)
admin.site.register(Payment,PaymentAdmin)
