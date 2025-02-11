# Generated by Django 5.1.5 on 2025-01-20 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aadhar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_no', models.IntegerField(unique=True)),
                ('created_by', models.CharField(max_length=50)),
                ('created_data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('aadhar', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='app.aadhar')),
            ],
        ),
    ]
