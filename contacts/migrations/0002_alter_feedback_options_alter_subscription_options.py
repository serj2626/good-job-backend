# Generated by Django 5.1 on 2024-11-10 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="feedback",
            options={
                "verbose_name": "Обратная связь",
                "verbose_name_plural": "Обратная связь",
            },
        ),
        migrations.AlterModelOptions(
            name="subscription",
            options={"verbose_name": "Подписка", "verbose_name_plural": "Подписки"},
        ),
    ]
