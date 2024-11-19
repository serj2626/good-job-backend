# Generated by Django 5.1 on 2024-11-19 13:26

import common.service
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_employee_options_alter_company_slug_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="resume",
            name="avatar",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=common.service.get_path_for_avatar,
                verbose_name="Аватар",
            ),
        ),
    ]
