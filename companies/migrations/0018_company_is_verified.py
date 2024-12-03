# Generated by Django 5.1 on 2024-12-01 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0017_alter_checkcompany_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="is_verified",
            field=models.BooleanField(
                blank=True, default=False, verbose_name="Проверенная компания"
            ),
        ),
    ]
