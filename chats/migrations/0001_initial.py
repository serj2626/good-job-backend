# Generated by Django 5.1 on 2025-02-16 10:46

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("companies", "0001_initial"),
        ("employees", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ResponseVacancy",
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
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создан"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Обновлен"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "Новый"),
                            ("accepted", "Приглашение"),
                            ("interview", "Интервью"),
                            ("offered", "Предложение на работу"),
                            ("rejected", "Отклонен"),
                        ],
                        default="new",
                        max_length=200,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "resume",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="all_responses",
                        to="employees.resume",
                        verbose_name="Резюме",
                    ),
                ),
                (
                    "vacancy",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="all_responses",
                        to="companies.vacancy",
                        verbose_name="Вакансия",
                    ),
                ),
            ],
            options={
                "verbose_name": "Отклик",
                "verbose_name_plural": "Отклики",
            },
        ),
        migrations.CreateModel(
            name="ResponseLetter",
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
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создан"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Обновлен"),
                ),
                (
                    "text",
                    models.TextField(max_length=5000, verbose_name="Текст письма"),
                ),
                (
                    "response_vacancy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="all_letters",
                        to="chats.responsevacancy",
                        verbose_name="Отклик",
                    ),
                ),
            ],
            options={
                "verbose_name": "Сопроводительное письмо",
                "verbose_name_plural": "Сопроводительные письма",
            },
        ),
        migrations.CreateModel(
            name="MessageToResponse",
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
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создан"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Обновлен"),
                ),
                (
                    "text",
                    models.TextField(max_length=1500, verbose_name="Текст сообщения"),
                ),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="response_vacancy_messages",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Получатель",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="my_messages",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Отправитель",
                    ),
                ),
                (
                    "response_vacancy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="all_messages",
                        to="chats.responsevacancy",
                        verbose_name="Отклик",
                    ),
                ),
            ],
            options={
                "verbose_name": "Сообщение отклика",
                "verbose_name_plural": "Сообщения отклика",
            },
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
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создан"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Обновлен"),
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
                    "date_interview",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата интервью"
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="interviews",
                        to="companies.company",
                        verbose_name="Компания",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="my_interviews",
                        to="employees.employee",
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
