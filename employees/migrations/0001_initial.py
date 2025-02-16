# Generated by Django 5.1 on 2025-02-16 10:46

import common.service
import django.db.models.deletion
import django.utils.timezone
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
                    "status",
                    models.CharField(
                        choices=[
                            ("unemployed", "Не ищу работу"),
                            ("search", "В поиске работы"),
                        ],
                        default="search",
                        max_length=300,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "position",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="Должность"
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=common.service.get_path_for_avatar_employee,
                        verbose_name="Аватар",
                    ),
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
                    "gender",
                    models.CharField(
                        choices=[
                            ("male", "Мужской"),
                            ("female", "Женский"),
                            ("other", "Не указано"),
                        ],
                        default="other",
                        max_length=255,
                        verbose_name="Пол",
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        blank=True,
                        default=django.utils.timezone.now,
                        null=True,
                        verbose_name="Дата рождения",
                    ),
                ),
                (
                    "stacks",
                    models.ManyToManyField(
                        blank=True, to="core.stack", verbose_name="Стек"
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
                "verbose_name": "Специалист",
                "verbose_name_plural": "Специалисты",
            },
        ),
        migrations.CreateModel(
            name="Education",
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
                    "start_month",
                    models.CharField(
                        choices=[
                            (1, "Январь"),
                            (2, "Февраль"),
                            (3, "Март"),
                            (4, "Апрель"),
                            (5, "Май"),
                            (6, "Июнь"),
                            (7, "Июль"),
                            (8, "Август"),
                            (9, "Сентябрь"),
                            (10, "Октябрь"),
                            (11, "Ноябрь"),
                            (12, "Декабрь"),
                        ],
                        max_length=200,
                        verbose_name="Месяц начала",
                    ),
                ),
                ("start_year", models.SmallIntegerField(verbose_name="Год начала")),
                (
                    "end_month",
                    models.CharField(
                        blank=True,
                        choices=[
                            (1, "Январь"),
                            (2, "Февраль"),
                            (3, "Март"),
                            (4, "Апрель"),
                            (5, "Май"),
                            (6, "Июнь"),
                            (7, "Июль"),
                            (8, "Август"),
                            (9, "Сентябрь"),
                            (10, "Октябрь"),
                            (11, "Ноябрь"),
                            (12, "Декабрь"),
                        ],
                        max_length=200,
                        null=True,
                        verbose_name="Месяц окончания",
                    ),
                ),
                (
                    "end_year",
                    models.SmallIntegerField(
                        blank=True, null=True, verbose_name="Год окончания"
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("univer", "Высшее образование"),
                            ("course", "Курсы"),
                            ("other", "Другое"),
                        ],
                        default="univer",
                        max_length=300,
                        verbose_name="Тип",
                    ),
                ),
                (
                    "university",
                    models.CharField(max_length=300, verbose_name="Университет"),
                ),
                (
                    "specialization",
                    models.CharField(max_length=300, verbose_name="Специализация"),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="educations",
                        to="employees.employee",
                        verbose_name="Работник",
                    ),
                ),
            ],
            options={
                "verbose_name": "Образование",
                "verbose_name_plural": "Образование",
            },
        ),
        migrations.CreateModel(
            name="Experience",
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
                    "start_month",
                    models.CharField(
                        choices=[
                            (1, "Январь"),
                            (2, "Февраль"),
                            (3, "Март"),
                            (4, "Апрель"),
                            (5, "Май"),
                            (6, "Июнь"),
                            (7, "Июль"),
                            (8, "Август"),
                            (9, "Сентябрь"),
                            (10, "Октябрь"),
                            (11, "Ноябрь"),
                            (12, "Декабрь"),
                        ],
                        max_length=200,
                        verbose_name="Месяц начала",
                    ),
                ),
                ("start_year", models.SmallIntegerField(verbose_name="Год начала")),
                (
                    "end_month",
                    models.CharField(
                        blank=True,
                        choices=[
                            (1, "Январь"),
                            (2, "Февраль"),
                            (3, "Март"),
                            (4, "Апрель"),
                            (5, "Май"),
                            (6, "Июнь"),
                            (7, "Июль"),
                            (8, "Август"),
                            (9, "Сентябрь"),
                            (10, "Октябрь"),
                            (11, "Ноябрь"),
                            (12, "Декабрь"),
                        ],
                        max_length=200,
                        null=True,
                        verbose_name="Месяц окончания",
                    ),
                ),
                (
                    "end_year",
                    models.SmallIntegerField(
                        blank=True, null=True, verbose_name="Год окончания"
                    ),
                ),
                ("company", models.CharField(max_length=300, verbose_name="Компания")),
                (
                    "position",
                    models.CharField(max_length=200, verbose_name="Должность"),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
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
                        related_name="experiences",
                        to="employees.employee",
                        verbose_name="Специалист",
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
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
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
                    "dislikes",
                    models.ManyToManyField(
                        blank=True,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Дизлайки",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="projects",
                        to="employees.employee",
                        verbose_name="Специалист",
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
            name="CommentProject",
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
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="employees.commentproject",
                        verbose_name="Родительский комментарий",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments_by_project",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="all_comments",
                        to="employees.project",
                        verbose_name="Проект",
                    ),
                ),
            ],
            options={
                "verbose_name": "Комментарий к проекту",
                "verbose_name_plural": "Комментарии к проекту",
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
                    "avatar",
                    models.ImageField(
                        blank=True,
                        default="employee/employee.jpg",
                        null=True,
                        upload_to=common.service.get_path_for_avatar_resume,
                        verbose_name="Аватар",
                    ),
                ),
                (
                    "about",
                    models.TextField(blank=True, null=True, verbose_name="О себе"),
                ),
                (
                    "is_visible",
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
                        related_name="resumes",
                        to="employees.employee",
                        verbose_name="Работник",
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
        migrations.CreateModel(
            name="SocialLinkEmployee",
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
                    "name",
                    models.CharField(
                        choices=[
                            ("vk", "Вконтакте"),
                            ("linkedin", "LinkedIn"),
                            ("tg", "Telegram"),
                            ("github", "GitHub"),
                            ("gitlab", "GitLab"),
                            ("habr", "Habr"),
                            ("other", "Другое"),
                        ],
                        max_length=300,
                        verbose_name="Название",
                    ),
                ),
                ("link", models.URLField(blank=True, null=True, verbose_name="Ссылка")),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employees.employee",
                        verbose_name="Специалист",
                    ),
                ),
            ],
            options={
                "verbose_name": "Социальная сеть",
                "verbose_name_plural": "Социальные сети",
            },
        ),
    ]
