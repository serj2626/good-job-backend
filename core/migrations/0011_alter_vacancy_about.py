# Generated by Django 5.1 on 2024-11-14 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_alter_vacancy_about_alter_vacancy_requirements"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vacancy",
            name="about",
            field=models.TextField(
                blank=True, max_length=3500, null=True, verbose_name="Описание"
            ),
        ),
    ]