# Generated by Django 5.1 on 2024-12-09 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0002_alter_company_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="about",
            field=models.TextField(blank=True, null=True, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Описание"),
        ),
    ]
