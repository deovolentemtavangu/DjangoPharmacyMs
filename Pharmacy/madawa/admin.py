from django.contrib import admin

from .models import medicine
from .models import order
from .models import inventory
from .models import Reports
from .models import customer
from .models import purchasing
from .models import Sales
from .models import pharmacist
from .models import Medicines

admin.site.register(medicine)
admin.site.register(order)
admin.site.register(inventory)

admin.site.register(Sales)
admin.site.register(customer)
admin.site.register(Reports)
admin.site.register(purchasing)
admin.site.register(pharmacist)
admin.site.register(Medicines)