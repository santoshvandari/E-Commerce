from django.contrib import admin
from store.models import Products, Category, Customer, Order

# Register your models here.
class AdminProducts(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'description', 'image']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email']

class AdminOrder(admin.ModelAdmin):
    list_display = ['product', 'customer', 'quantity', 'price', 'address', 'phone', 'date']

admin.site.register(Products, AdminProducts)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)


