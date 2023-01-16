
from django.contrib import admin
from django.urls import path, include
from madawa import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('madawa.urls')),
    path('API/', include('API.urls')),
    path('create-project', views.createProject, name="create-project"),
    path('create-inventory', views.createInventory, name="create-inventory"),
    path('create-order', views.createOrder, name="create-order"),
    path('update-project',views.updateProject, name="update-project"),

    path('create-report',views.createReport, name="create-report"),
    path('create-sales',views.createSales, name="create-sales"),
    path('create-purchasing',views.createPurchasing, name="create-purchasing"),
    path('create-customer',views.createCustomer, name="create-customer"),
    path('create-pharmacist',views.createPharmacist, name="create-pharmacist"),
    path('create-medicines',views.createMedicines, name="create-medicines"),
    
]
