# Generated by Django 5.1 on 2024-12-01 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0013_checkcompany_consent"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="type",
            field=models.CharField(
                choices=[
                    ("OOO", "ООО"),
                    ("IP", "ИП"),
                    ("UP", "УП"),
                    ("PAO", "ПАО"),
                    ("Corp", "Corp"),
                    ("ZAO", "ЗАО"),
                    ("OAO", "ОАО"),
                    ("AO", "АО"),
                    ("other", "Другое"),
                ],
                default="OOO",
                max_length=30,
                verbose_name="Тип компании",
            ),
        ),
    ]
