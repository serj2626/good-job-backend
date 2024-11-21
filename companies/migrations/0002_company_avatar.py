# Generated by Django 5.1 on 2024-11-21 11:27

import common.service
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="avatar",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=common.service.get_path_for_avatar_company,
                verbose_name="Аватар",
            ),
        ),
    ]
