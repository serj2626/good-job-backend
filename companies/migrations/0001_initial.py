# Generated by Django 5.1 on 2025-02-16 10:46

import common.service
import django.core.validators
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
            name="Company",
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
                    "about",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True, null=True, unique=True, verbose_name="Слаг"
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("OOO", "ООО"),
                            ("IP", "ИП"),
                            ("UP", "УП"),
                            ("PAO", "ПАО"),
                            ("Corp", "Corp"),
                            ("ZAO", "ЗАО"),
                            ("OAO", "ОАО"),
                            ("AO", "АО"),
                            ("other", "Другое"),
                        ],
                        default="OOO",
                        max_length=30,
                        verbose_name="Тип компании",
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        default="company/company.jpg",
                        null=True,
                        upload_to=common.service.get_path_for_avatar_company,
                        verbose_name="Аватар",
                    ),
                ),
                (
                    "count_employees",
                    models.SmallIntegerField(
                        default=0, verbose_name="Количество  сотрудников"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="Название компании",
                    ),
                ),
                (
                    "site",
                    models.URLField(
                        blank=True, null=True, verbose_name="Сайт компании"
                    ),
                ),
                (
                    "is_verified",
                    models.BooleanField(
                        blank=True, default=False, verbose_name="Проверенная компания"
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
                "verbose_name": "Компания",
                "verbose_name_plural": "Компании",
            },
        ),
        migrations.CreateModel(
            name="CommentCompany",
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
                ("text", models.TextField(max_length=3000, verbose_name="Сообщение")),
                (
                    "stars",
                    models.SmallIntegerField(
                        default=5,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                        verbose_name="Оценка",
                    ),
                ),
                (
                    "dislikes",
                    models.ManyToManyField(
                        blank=True,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Дизлайки",
                    ),
                ),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Лайки",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments_by_company",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="all_comments",
                        to="companies.company",
                        verbose_name="Компания",
                    ),
                ),
            ],
            options={
                "verbose_name": "Комментарий к компании",
                "verbose_name_plural": "Комментарии к компании",
            },
        ),
        migrations.CreateModel(
            name="CheckCompany",
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
                    "egrul",
                    models.FileField(
                        upload_to=common.service.get_path_for_check_company_egrul,
                        verbose_name="Выписка из ЕГРЮЛ и ЕГРИП",
                    ),
                ),
                (
                    "certificate",
                    models.FileField(
                        upload_to=common.service.get_path_for_check_company_certificate,
                        verbose_name="Cвидетельство о регистрации фирмы или ИП",
                    ),
                ),
                (
                    "certificate_nalog",
                    models.FileField(
                        upload_to=common.service.get_path_for_check_company_certificate_nalog,
                        verbose_name="Cправка о постановке на учет в налоговом органе",
                    ),
                ),
                (
                    "constitution",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=common.service.get_path_for_check_company_constitution,
                        verbose_name="Устав",
                    ),
                ),
                (
                    "license",
                    models.FileField(
                        upload_to=common.service.get_path_for_check_company_license,
                        verbose_name="Лицензия на необходимые виды деятельности",
                    ),
                ),
                (
                    "no_debt",
                    models.FileField(
                        upload_to=common.service.get_path_for_check_company_no_debt,
                        verbose_name="Справка, подтверждающая отсутствие налоговых задолженностей",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("sent", "Отправлено"),
                            ("pending", "На расмотрении"),
                            ("accepted", "Принято"),
                            ("rejected", "Отклонено"),
                        ],
                        default="pending",
                        max_length=200,
                        verbose_name="Статус проверки",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="checks",
                        to="companies.company",
                        verbose_name="Компания",
                    ),
                ),
            ],
            options={
                "verbose_name": "Проверка компании",
                "verbose_name_plural": "Проверки компании",
            },
        ),
        migrations.CreateModel(
            name="Vacancy",
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
                    "currency",
                    models.CharField(
                        choices=[("RUB", "RUB"), ("USD", "USD"), ("EUR", "EUR")],
                        default="RUB",
                        max_length=200,
                        verbose_name="Валюта",
                    ),
                ),
                (
                    "work_schedule",
                    models.CharField(
                        choices=[
                            ("full-time", "Полный рабочий день"),
                            ("part-time", "Частичная занятость"),
                            ("project", "Проектная работа"),
                        ],
                        default="full-time",
                        max_length=200,
                        verbose_name="График работы",
                    ),
                ),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("none", "Не имеет значения"),
                            ("intern", "Стажер"),
                            ("junior", "Junior"),
                            ("junior_plus", "Junior+"),
                            ("middle", "Middle"),
                            ("middle_plus", "Middle+"),
                            ("senior", "Senior"),
                            ("team_lead", "Team Lead"),
                        ],
                        default="junior",
                        max_length=200,
                        verbose_name="Уровень",
                    ),
                ),
                (
                    "status_vacancy",
                    models.CharField(
                        choices=[("open", " Открыта"), ("archived", "В архиве")],
                        default="open",
                        max_length=200,
                        verbose_name="Статус вакансии",
                    ),
                ),
                (
                    "format_work",
                    models.CharField(
                        choices=[
                            ("office", "В офисе"),
                            ("remote", "Удаленная работа"),
                            ("hybrid", "Гибридная работа"),
                        ],
                        default="remote",
                        max_length=200,
                        verbose_name="Формат работы",
                    ),
                ),
                (
                    "work_experience",
                    models.SmallIntegerField(
                        blank=True, null=True, verbose_name="Стаж"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="Город"
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="Страна"
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
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
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vacancies",
                        to="companies.company",
                        verbose_name="Компания",
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
                "verbose_name": "Вакансия",
                "verbose_name_plural": "Вакансии",
            },
        ),
    ]
