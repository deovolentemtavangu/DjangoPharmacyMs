import datetime
import uuid
from django.db import models



class medicine(models.Model):
    UNIT_FORM = (
    ('Mg', 'Mg'),
    ('Ml','ml'),
    )
    name = models.CharField(max_length=200)
    strength = models.CharField(max_length=200)
    description =models.CharField(max_length=200)
    unit = models.CharField(max_length=50, choices=UNIT_FORM)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)

    def __str__(self):
      return self.name

class order(models.Model):
  ORDER_FORM = (
   ('tablets', 'tablets'),
   ('ointment','ointment'),
   ('liquid','liquid'),
  )
  order_name = models.CharField(max_length=200)
  order_type = models.CharField(max_length=200, choices=ORDER_FORM)
  order_type_id = models.IntegerField
  customer_name = models.CharField(max_length=200)
  id = models.IntegerField

  def __str__(self):
    return self.order_name

class inventory(models.Model):
  INVENTORY_FORM = (
   ('Main Pharmacy', 'Main Pharmacy'),
   ('Sub Pharmacy','Sub Pharmacy'),
  )
  inventory_name = models.CharField(max_length=200)
  inventory_type = models.CharField(max_length=200, choices=INVENTORY_FORM)
  inventory_id = models.IntegerField
  
  def __str__(self):
    return self.inventory_name


class Medicines(models.Model):
  med_id = models.IntegerField
  med_category = models.CharField(max_length=200)
  name = models.CharField(max_length=200)
  Description = models.TextField()
  price = models.IntegerField

  def __str__(self):
    return self.name

class customer(models.Model):
  GENDER =(
     ('MALE','MALE'),
    ('FEMALE','FEMALE')
    )
  cust_id = models.IntegerField
  fname = models.CharField(max_length=200)
  lname = models.CharField(max_length=200)
  gender = models.CharField(max_length=200, choices=GENDER)
  age = models.FloatField()
  contact_add = models.CharField(max_length=200)
  cust_email = models.CharField(max_length=200)
  cust_pass = models.CharField(max_length=200)

  def __str__(self):
    return  self.fname
  
class pharmacist(models.Model):
  GENDER =(
     ('MALE','MALE'),
    ('FEMALE','FEMALE')
    )
  phar_id = models.IntegerField
  fname = models.CharField(max_length=200)
  lname = models.CharField(max_length=200)
  gender = models.CharField(max_length=200, choices=GENDER)
  age = models.FloatField()
  admin_add = models.CharField(max_length=200)
  admin_email = models.CharField(max_length=200)
  admin_pass = models.CharField(max_length=200)

  def __str__(self):
    return  self.fname
  

class purchasing(models.Model):
  purchase_id = models.IntegerField
  cust_id = models.ForeignKey(customer, models.CASCADE)
  med_id = models.ForeignKey(Medicines, models.CASCADE)
  amount = models.CharField(max_length=200)
  date = models.DateTimeField(auto_now_add = True)
  
  def __str__(self):
    return self.amount

class Sales(models.Model):
  sales_id = models.IntegerField
  phar_id = models.ForeignKey(pharmacist, models.CASCADE)
  cust_id = models.ForeignKey(customer, models.CASCADE)
  med_id = models.ForeignKey(Medicines, models.CASCADE)
  count = models.CharField(max_length=200)
  purchase_id =models.ForeignKey(purchasing, models.CASCADE)
  date = models.DateTimeField(auto_now_add = True)
  total_amount = models.CharField(max_length=200)

  def __str__(self):
    return self.count


class Reports(models.Model):
  report_id = models.IntegerField
  purchase_id = models.ForeignKey(purchasing, models.CASCADE)
  sales_id = models.ForeignKey(Sales, models.CASCADE)
  cust_id = models.ForeignKey(customer, models.CASCADE)
  date = models.DateTimeField(auto_now_add = True)
  
  def __str__(self):
    return self.report_id


