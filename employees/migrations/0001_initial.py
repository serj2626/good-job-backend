# Generated by Django 5.1 on 2024-11-21 09:31

import common.service
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Телефон"
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True,
                        default="Россия",
                        max_length=255,
                        null=True,
                        verbose_name="Страна",
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True,
                        default="Москва",
                        max_length=255,
                        null=True,
                        verbose_name="Город",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True, null=True, unique=True, verbose_name="Слаг"
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
                    "first_name",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Имя"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Фамилия"
                    ),
                ),
                (
                    "middle_name",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Отчество"
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата рождения"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Работник",
                "verbose_name_plural": "Работники",
            },
        ),
        migrations.CreateModel(
            name="Experience",
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
                ("company", models.CharField(max_length=300, verbose_name="Компания")),
                (
                    "position",
                    models.CharField(max_length=200, verbose_name="Должность"),
                ),
                (
                    "requirements",
                    models.TextField(
                        blank=True,
                        max_length=3000,
                        null=True,
                        verbose_name="Требования",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=3500, null=True, verbose_name="Описание"
                    ),
                ),
                ("start_date", models.DateField(verbose_name="Начало работы")),
                (
                    "end_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Окончание работы"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.category",
                        verbose_name="Категория",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employees.employee",
                        verbose_name="Работник",
                    ),
                ),
                (
                    "stacks",
                    models.ManyToManyField(to="core.stack", verbose_name="Стек"),
                ),
            ],
            options={
                "verbose_name": "Опыт работы",
                "verbose_name_plural": "Опыт работы",
            },
        ),
        migrations.CreateModel(
            name="Project",
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
                (
                    "title",
                    models.CharField(max_length=300, verbose_name="Название проекта"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=common.service.get_path_for_image_project,
                        verbose_name="Постер",
                    ),
                ),
                (
                    "link",
                    models.URLField(
                        blank=True, null=True, verbose_name="Ссылка на проект"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=3000, null=True, verbose_name="Описание"
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
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.category",
                        verbose_name="Категория",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employees.employee",
                        verbose_name="Работник",
                    ),
                ),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True, to=settings.AUTH_USER_MODEL, verbose_name="Лайки"
                    ),
                ),
                (
                    "stacks",
                    models.ManyToManyField(
                        blank=True, to="core.stack", verbose_name="Стек"
                    ),
                ),
            ],
            options={
                "verbose_name": "Проект",
                "verbose_name_plural": "Проекты",
            },
        ),
        migrations.CreateModel(
            name="Resume",
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
                    "position",
                    models.CharField(max_length=200, verbose_name="Должность"),
                ),
                (
                    "min_salary",
                    models.SmallIntegerField(
                        blank=True, null=True, verbose_name="Минимальная зарплата"
                    ),
                ),
                (
                    "max_salary",
                    models.SmallIntegerField(
                        blank=True, null=True, verbose_name="Максимальная зарплата"
                    ),
                ),
                (
                    "work_schedule",
                    models.CharField(
                        choices=[
                            ("full-time", "Полный рабочий день"),
                            ("part-time", "Частичная занятость"),
                            ("remote", "Удаленная работа"),
                        ],
                        default="full-time",
                        max_length=200,
                        verbose_name="График работы",
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
                    "avatar",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=common.service.get_path_for_avatar,
                        verbose_name="Аватар",
                    ),
                ),
                (
                    "about",
                    models.TextField(
                        blank=True, max_length=1000, null=True, verbose_name="О себе"
                    ),
                ),
                (
                    "visibility",
                    models.BooleanField(default=True, verbose_name="Видимость"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.category",
                        verbose_name="Категория",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employees.employee",
                        verbose_name="Работник",
                    ),
                ),
                (
                    "experience",
                    models.ManyToManyField(
                        blank=True,
                        to="employees.experience",
                        verbose_name="Опыт работы",
                    ),
                ),
                (
                    "stacks",
                    models.ManyToManyField(
                        blank=True, to="core.stack", verbose_name="Стек"
                    ),
                ),
            ],
            options={
                "verbose_name": "Резюме",
                "verbose_name_plural": "Резюме",
            },
        ),
    ]
