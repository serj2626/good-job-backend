# Generated by Django 5.1 on 2024-11-10 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_stack"),
    ]

    operations = [
        migrations.AddField(
            model_name="resume",
            name="stacks",
            field=models.ManyToManyField(to="core.stack", verbose_name="Стек"),
        ),
        migrations.AddField(
            model_name="vacancy",
            name="stacks",
            field=models.ManyToManyField(to="core.stack", verbose_name="Стек"),
        ),
    ]
