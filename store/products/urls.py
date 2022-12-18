from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='Index'),
    path('products', views.products, name='Products')
]