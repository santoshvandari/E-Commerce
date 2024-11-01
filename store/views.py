from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from store.models import Products, Category, Customer, Order
from store.validate_customer import validate_customer


# Signup view
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    
    if request.method == 'POST':
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=password
        )

        error_message = validate_customer(customer)

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('login')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)


# Login view
def login_view(request):
    if request.method == 'GET':
        request.session['return_url'] = request.GET.get('return_url')
        return render(request, 'login.html')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None

        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                return_url = request.session.get('return_url')
                if return_url:
                    del request.session['return_url']
                    return HttpResponseRedirect(return_url)
                else:
                    return redirect('homepage')
            else:
                error_message = 'Invalid Password!'
        else:
            error_message = 'Invalid Email or Password!'

        return render(request, 'login.html', {'error': error_message})

# Logout view
def logout_view(request):
    request.session.clear()
    return redirect('login')


# Homepage view
def index(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart:', request.session['cart'])
        return redirect('homepage')
    
    return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

# Store view
def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}

    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products()

    data = {
        'products': products,
        'categories': categories
    }
    
    print('you are:', request.session.get('email'))
    return render(request, 'index.html', data)

# Cart view (requires authentication)
def cart(request):
    if not request.session.get('customer'):
        return redirect('login')

    cart = request.session.get('cart')
    products = Products.get_products_by_id(list(cart.keys()))
    total = sum(item.price * cart[str(item.id)] for item in products)
    return render(request, 'cart.html', {'products': products, 'total': total})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    

    return redirect('cart')


# Checkout view (requires authentication)
def checkout(request):
    if not request.session.get('customer'):
        return redirect('login')

    if request.method == 'POST':
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))

        for product in products:
            order = Order(
                customer=Customer(id=customer),
                product=product,
                price=product.price,
                address=address,
                phone=phone,
                quantity=cart.get(str(product.id))
            )
            order.save()

        request.session['cart'] = {}
        return redirect('cart')

# Order view (requires authentication)
def order_view(request):
    if not request.session.get('customer'):
        return redirect('login')

    customer = request.session.get('customer')
    orders = Order.get_orders_by_customer(customer)
    return render(request, 'orders.html', {'orders': orders})
