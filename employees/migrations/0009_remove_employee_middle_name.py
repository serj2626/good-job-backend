# Generated by Django 5.1 on 2024-11-24 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0008_employee_gender"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employee",
            name="middle_name",
        ),
    ]
