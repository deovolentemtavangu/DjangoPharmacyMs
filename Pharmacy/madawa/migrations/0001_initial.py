# Generated by Django 4.1.4 on 2022-12-31 00:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='medicine',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('strength', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('unit', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
