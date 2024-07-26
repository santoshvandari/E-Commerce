from django.urls import path
from Auth.views import views

urlpatterns = [
    path('/login', views.log_in, name='signin'),
    path('/register', views.sign_up, name='signup'),
]
