# Generated by Django 5.1 on 2024-11-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0002_company_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="about",
            field=models.TextField(
                blank=True, max_length=5000, null=True, verbose_name="Описание"
            ),
        ),
    ]