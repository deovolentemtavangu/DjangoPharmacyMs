from os import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import inventory, medicine, order,Sales,purchasing,Reports,Medicines,customer,pharmacist
from .forms import ProjectForm, InventoryForm, OrderForm,ReportsForm,SalesForm,PurchasingForm,CustomerForm,MedicinesForm,PharmacistForm

def home(request):
    return render(request, 'madawa/home.html')

def mediciness(request):
    medicines_list = Medicines.objects.all()
    medicine_count = Medicines.objects.count()
    context = {'medicines_list': medicines_list ,'medicine_count': medicine_count  }
    return render(request, 'madawa/medicines.html', context)

def reportss(request):
    reports_list = Reports.objects.all()
    report_count = Reports.objects.count()
    context = {'reports_list': reports_list ,'report_count' : report_count }
    return render(request, 'madawa/reports.html', context)

def customers(request):
    customer_list = customer.objects.all()
    context = {'customer_list': customer_list }
    return render(request, 'madawa/customers.html', context)

def purchasings(request):
    purchasing_list = purchasing.objects.all()
    context = {'purchasing_list': purchasing_list }
    return render(request, 'madawa/purchasing.html', context)


def pharmacists(request):
    pharmacist_list = pharmacist.objects.all()
    context = {'pharmacist_list': pharmacist_list }
    return render(request, 'madawa/pharmacist.html', context)

def saless(request):
    sales_list = Sales.objects.all()
    context = {'sales_list': sales_list }
    return render(request, 'madawa/sales.html', context)

def inventories(request):
    inventory_list = inventory.objects.all()
    context = {'inventory_list': inventory_list }
    return render(request, 'madawa/inventory.html', context)


def orders(request):
    order_list = order.objects.all()
    context = {'order_list': order_list}
    return render(request, 'madawa/orders.html', context)

def products(request):
     medicine_list = medicine.objects.all()
     return render(request, 'madawa/products.html', {'medicine_list':medicine_list})

def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        print(request.POST)
        form = ProjectForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('products')
    context = {'form':form}
    return render(request, 'madawa/project_form.html', context)

def updateProject(request,pk):
    project = medicine.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        print(request.POST)
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
             form.save()
             return redirect('products')
    context = {'form':form}
    return render(request, 'madawa/project_form.html', context)


def createInventory(request):
    form = InventoryForm()

    if request.method == 'POST':
        print(request.POST)
        form = InventoryForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('inventories')
    context = {'form':form}
    return render(request, 'madawa/inventory_form.html', context)

def createOrder(request):
    form = OrderForm()

    if request.method == 'POST':
        print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('orders')
    context = {'form':form}
    return render(request, 'madawa/order_form.html', context)


def createReport(request):
    form = ReportsForm()

    if request.method == 'POST':
        print(request.POST)
        form = ReportsForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('reports')
    context = {'form':form}
    return render(request, 'madawa/report_form.html', context)

def createCustomer(request):
    form = CustomerForm()

    if request.method == 'POST':
        print(request.POST)
        form = CustomerForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('customers')
    context = {'form':form}
    return render(request, 'madawa/customer_form.html', context)

def createPharmacist(request):
    form = PharmacistForm()

    if request.method == 'POST':
        print(request.POST)
        form = PharmacistForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('pharmacist')
    context = {'form':form}
    return render(request, 'madawa/pharmacist_form.html', context)

def createSales(request):
    form = SalesForm()

    if request.method == 'POST':
        print(request.POST)
        form = SalesForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('sales')
    context = {'form':form}
    return render(request, 'madawa/sales_form.html', context)

def createMedicines(request):
    form = MedicinesForm()

    if request.method == 'POST':
        print(request.POST)
        form = MedicinesForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('medicines')
    context = {'form':form}
    return render(request, 'madawa/medicines_form.html', context)

def createPurchasing(request):
    form = PurchasingForm()

    if request.method == 'POST':
        print(request.POST)
        form = PurchasingForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('purchasing')
    context = {'form':form}
    return render(request, 'madawa/purchasing_form.html', context)