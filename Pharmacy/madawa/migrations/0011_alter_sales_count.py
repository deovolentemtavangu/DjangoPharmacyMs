# Generated by Django 4.1.4 on 2023-01-09 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madawa', '0010_alter_sales_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='count',
            field=models.CharField(max_length=200),
        ),
    ]