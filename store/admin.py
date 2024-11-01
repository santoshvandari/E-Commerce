from django.contrib import admin
from store.models import Products, Category, Customer, Order

# Register your models here.
class AdminProducts(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'description', 'image']
    search_fields = ['name', 'category__name']  # Adding search functionality
    list_filter = ['category']  # Filter by category

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']  # Adding search functionality

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email']
    search_fields = ['email', 'phone']  # Adding search functionality

class AdminOrder(admin.ModelAdmin):
    list_display = ['product', 'customer', 'quantity', 'price', 'date', 'status']
    list_filter = ['status', 'date']  # Filter by order status and date
    search_fields = ['customer__email', 'product__name']  # Adding search functionality

# Registering the models with their respective admin classes
admin.site.register(Products, AdminProducts)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)
