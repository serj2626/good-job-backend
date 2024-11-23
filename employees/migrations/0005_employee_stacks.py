# Generated by Django 5.1 on 2024-11-21 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
        ("employees", "0004_sociallinkemployee"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="stacks",
            field=models.ManyToManyField(
                blank=True, to="core.stack", verbose_name="Стек"
            ),
        ),
    ]