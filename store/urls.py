from django.urls import path 
from store.views import index, store, signup, login_view, logout_view, cart, checkout, order_view

urlpatterns = [ 
    path('', index, name='homepage'), 
    path('store', store, name='store'), 
    path('signup', signup, name='signup'), 
    path('login', login_view, name='login'), 
    path('logout', logout_view, name='logout'), 
    path('cart', cart, name='cart'), 
    path('check-out', checkout, name='checkout'), 
    path('orders', order_view, name='orders'), 
]
