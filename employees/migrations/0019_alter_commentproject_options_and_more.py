# Generated by Django 5.1 on 2024-11-28 13:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0018_employee_middle_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="commentproject",
            options={
                "verbose_name": "Комментарий к проекту",
                "verbose_name_plural": "Комментарии к проекту",
            },
        ),
        migrations.AlterField(
            model_name="employee",
            name="date_of_birth",
            field=models.DateField(
                blank=True,
                default=django.utils.timezone.now,
                null=True,
                verbose_name="Дата рождения",
            ),
        ),
        migrations.AlterField(
            model_name="resume",
            name="work_schedule",
            field=models.CharField(
                choices=[
                    ("full-time", "Полный рабочий день"),
                    ("part-time", "Частичная занятость"),
                    ("remote", "Удаленная работа"),
                    ("hybrid", "Гибридная работа"),
                ],
                default="full-time",
                max_length=200,
                verbose_name="График работы",
            ),
        ),
    ]
