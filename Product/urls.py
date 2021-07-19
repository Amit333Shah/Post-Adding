from django.urls import path
from .import views

urlpatterns=[
    path('Product',views.Product, name="Product"),
]