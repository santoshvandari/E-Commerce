from django.urls import path
from store import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('home/', views.Home, name='home'),

]
