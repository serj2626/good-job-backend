# Generated by Django 5.1 on 2024-11-10 19:29

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chats", "0002_alter_responsevacancy_resume_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="responsevacancy",
            name="status",
            field=models.CharField(
                choices=[
                    ("new", "Новый"),
                    ("accepted", "Принят"),
                    ("interview", "Интервью"),
                    ("offered", "Предложение на работу"),
                    ("rejected", "Отклонен"),
                ],
                default="new",
                max_length=200,
                verbose_name="Статус",
            ),
        ),
        migrations.CreateModel(
            name="Interview",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "Создан"),
                            ("finished", "Окончен"),
                            ("canceled", "Отменен"),
                            ("accepted", "Успешен"),
                            ("rejected", "Отклонен"),
                        ],
                        default="new",
                        max_length=200,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создан"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Обновлен"),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="interviews",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Компания",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="my_interviews",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Работник",
                    ),
                ),
                (
                    "response_vacancy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="all_interviews",
                        to="chats.responsevacancy",
                        verbose_name="Отклик",
                    ),
                ),
            ],
            options={
                "verbose_name": "Интервью",
                "verbose_name_plural": "Интервью",
            },
        ),
    ]
