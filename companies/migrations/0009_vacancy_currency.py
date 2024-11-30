# Generated by Django 5.1 on 2024-11-29 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0008_alter_vacancy_min_salary"),
    ]

    operations = [
        migrations.AddField(
            model_name="vacancy",
            name="currency",
            field=models.CharField(
                choices=[("RUB", "RUB"), ("USD", "USD"), ("EUR", "EUR")],
                default="RUB",
                max_length=200,
                verbose_name="Валюта",
            ),
        ),
    ]
