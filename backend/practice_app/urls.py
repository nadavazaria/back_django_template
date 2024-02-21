"""app urls make shit happen over here """
from django.contrib import admin
from django.urls import path
from .views import MyTokenObtainPairView
from . import views
urlpatterns = [
    path('', views.index),
    path('products', views.get_prods),
    path('update_product/<int:id>', views.update_prod),
    path('add_product', views.add_prod),
    path('delete_product/<int:id>', views.delete_prod),
    path('login', MyTokenObtainPairView.as_view()),
    path('register', views.register),
]
