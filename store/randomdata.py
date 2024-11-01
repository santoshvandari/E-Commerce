from faker import Faker
from store.models import Category, Products, Customer, Order
import random

fake = Faker()

# Step 1: Create some categories
categories = []
for _ in range(5):
    category = Category(name=fake.word())
    category.save()
    categories.append(category)

# Step 2: Create products for each category
for _ in range(20):  # Generating 20 products
    product = Products(
        name=fake.word().capitalize(),
        price=random.randint(10, 1000),  # Random price between 10 and 1000
        category=random.choice(categories),
        description=fake.sentence(nb_words=8),
        image='uploads/products/sample.jpg'  # Using a placeholder path for the image
    )
    product.save()

# Step 3: Create some customers
customers = []
for _ in range(10):  # Generating 10 customers
    customer = Customer(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        phone=fake.phone_number()[:10],  # Truncate to fit the 10-char limit
        email=fake.email(),
        password=fake.password()
    )
    customer.save()
    customers.append(customer)

# Step 4: Create some orders
for _ in range(15):  # Generating 15 orders
    order = Order(
        product=random.choice(Products.objects.all()),
        customer=random.choice(customers),
        quantity=random.randint(1, 5),
        price=random.randint(50, 1000),
        address=fake.address(),
        phone=fake.phone_number()[:10],  # Truncate to fit the 10-char limit
        date=fake.date_between(start_date='-1y', end_date='today'),  # Date within the last year
        status=random.choice([True, False])
    )
    order.save()

print("Dummy data inserted successfully.")
