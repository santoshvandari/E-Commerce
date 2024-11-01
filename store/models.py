from django.db import models
import datetime
# Create your models here.
class Category(models.Model): 
    name = models.CharField(max_length=50) 
  
    @staticmethod
    def get_all_categories(): 
        return Category.objects.all() 
  
    def __str__(self): 
        return self.name 

class Products(models.Model): 
    name = models.CharField(max_length=60) 
    price = models.IntegerField(default=0) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1) 
    description = models.CharField( 
        max_length=250, default='', blank=True, null=True) 
    image = models.ImageField(upload_to='media/products/') 
  
    @staticmethod
    def get_products_by_id(ids): 
        return Products.objects.filter(id__in=ids) 
  
    @staticmethod
    def get_all_products(): 
        return Products.objects.all() 
  
    @staticmethod
    def get_all_products_by_categoryid(category_id): 
        if category_id: 
            return Products.objects.filter(category=category_id) 
        else: 
            return Products.get_all_products() 
    
class Customer(models.Model): 
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50) 
    phone = models.CharField(max_length=10) 
    email = models.EmailField() 
    password = models.CharField(max_length=100) 
  
    # to save the data 
    def register(self): 
        self.save() 
  
    @staticmethod
    def get_customer_by_email(email): 
        try: 
            return Customer.objects.get(email=email) 
        except: 
            return False
  
    def isExists(self): 
        if Customer.objects.filter(email=self.email): 
            return True
  
        return False
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled')
    ]
    
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Use DecimalField for currency
    address = models.CharField(max_length=255, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.date.today)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def place_order(self):
        self.save()

    def total_price(self):
        return self.price * self.quantity  # Calculate total price

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

    def __str__(self):
        return f"Order {self.id} - {self.product.name} for {self.customer.first_name}"

