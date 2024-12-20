# Generated by Django 5.1 on 2024-12-06 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("companies", "0001_initial"),
        ("employees", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="NotificationCompany",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("new_vacancy", "Новая вакансия"),
                            ("new_interview", "Новое интервью"),
                            ("new_message", "Новое сообщение"),
                            ("new_response", "Новый отклик"),
                            ("archive_vacancy", "Вакансия перенесена в архив"),
                            ("new_user", "На вас подписался новый пользователь"),
                            ("new_visitor", "Вашу страницу посетил новый пользователь"),
                        ],
                        max_length=255,
                    ),
                ),
                ("read", models.BooleanField(default=False, verbose_name="Прочитано")),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="companies.company",
                    ),
                ),
            ],
            options={
                "verbose_name": "Уведомление компании",
                "verbose_name_plural": "Уведомления компаний",
            },
        ),
        migrations.CreateModel(
            name="NotificationEmployee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("new_vacancy", "Новая вакансия"),
                            ("new_interview", "Новое интервью"),
                            ("new_message", "Новое сообщение"),
                            ("new_response", "Новый отклик"),
                            ("archive_vacancy", "Вакансия перенесена в архив"),
                            ("new_user", "На вас подписался новый пользователь"),
                            ("new_visitor", "Вашу страницу посетил новый пользователь"),
                        ],
                        max_length=255,
                    ),
                ),
                ("read", models.BooleanField(default=False, verbose_name="Прочитано")),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employees.employee",
                    ),
                ),
            ],
            options={
                "verbose_name": "Уведомление работника",
                "verbose_name_plural": "Уведомления работников",
            },
        ),
    ]
