# Generated by Django 5.1.5 on 2025-01-23 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_vehicle_remove_student_student_dep_fuel_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fuel',
            old_name='v_nm',
            new_name='v_name',
        ),
    ]
