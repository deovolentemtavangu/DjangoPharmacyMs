# Generated by Django 4.1.4 on 2022-12-31 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madawa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(max_length=200)),
                ('order_type', models.CharField(max_length=200)),
                ('customer_name', models.CharField(max_length=200)),
                ('Order_number', models.CharField(max_length=200)),
            ],
        ),
    ]
