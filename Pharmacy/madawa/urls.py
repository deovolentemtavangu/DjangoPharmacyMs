from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('Inventory/', views.inventories, name="inventories"),
    path('Products/', views.products, name="products"),
    path('Orders/', views.orders, name="orders"),
    path('Reports/', views.reportss, name="reports"),
    path('Purchasing/', views.purchasings, name="purchasing"),
    path('Pharmacist/', views.pharmacists, name="pharmacist"),
    path('Medicines/', views.mediciness, name="medicines"),
    path('Reports/', views.reportss, name="repors"),
    path('Sales/', views.saless, name="sales"),
    path('customer/', views.customers, name="customer")   
]
