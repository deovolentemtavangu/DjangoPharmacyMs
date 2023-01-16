from django.forms import ModelForm
from .models import medicine, inventory, order, Medicines ,Reports,customer,purchasing,pharmacist,Sales

class ProjectForm(ModelForm):
    class Meta:
        model = medicine
        fields = '__all__'

class InventoryForm(ModelForm):
    class Meta:
        model = inventory
        fields = '__all__'

class OrderForm(ModelForm):
    class Meta:
        model = order
        fields = '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model = customer
        fields = '__all__'


class SalesForm(ModelForm):
    class Meta:
        model = Sales
        fields = '__all__'

class ReportsForm(ModelForm):
    class Meta:
        model = Reports
        fields = '__all__'
    

class PharmacistForm(ModelForm):
    class Meta:
        model = pharmacist
        fields = '__all__'

class MedicinesForm(ModelForm):
    class Meta:
        model = Medicines
        fields = '__all__'

class PurchasingForm(ModelForm):
    class Meta:
        model = purchasing
        fields = '__all__'