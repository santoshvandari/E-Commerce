from django.urls import path
from Auth import views

urlpatterns = [
    path('login/', views.log_in, name='signin'),
    path('register/', views.sign_up, name='signup'),
    path('logout/',views.log_out,name='logout')
]
