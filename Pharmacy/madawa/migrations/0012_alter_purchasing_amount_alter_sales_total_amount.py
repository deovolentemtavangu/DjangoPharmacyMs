# Generated by Django 4.1.4 on 2023-01-09 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madawa', '0011_alter_sales_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasing',
            name='amount',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='sales',
            name='total_amount',
            field=models.CharField(max_length=200),
        ),
    ]
