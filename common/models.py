from django.db import models
import uuid
from django.core.exceptions import ValidationError
from accounts.models import User
from core.models import Category, Stack
from common.const import CURRENCY_TYPE, WORK_SCHEDULE, MONTHS
from django.core.validators import MinValueValidator, MaxValueValidator


class MyBaseModel(models.Model):
    """
    Абстрактная модель для общих полей.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    class Meta:
        abstract = True


class EducationOrExperienceModel(MyBaseModel):
    """
    Абстрактная модель для образования или опыта.
    """

    start_month = models.CharField("Месяц начала", max_length=200, choices=MONTHS)
    start_year = models.SmallIntegerField("Год начала")
    end_month = models.CharField(
        "Месяц окончания", max_length=200, choices=MONTHS, blank=True, null=True
    )
    end_year = models.SmallIntegerField("Год окончания", blank=True, null=True)

    class Meta:
        abstract = True

    def clear(self):
        if self.start_year > self.end_year:
            raise ValidationError("Год окончания не может быть меньше года начала")
        if self.start_year == self.end_year:
            if self.start_month > self.end_month:
                raise ValidationError(
                    "Месяц окончания не может быть меньше месяца начала"
                )
            if self.start_month == self.end_month:
                raise ValidationError("Год и месяц окончания не могут быть одинаковыми")

        return super().clean()


class CommentBaseModel(MyBaseModel):
    """
    Абстрактная модель для комментариев.
    """

    likes = models.ManyToManyField(
        User, verbose_name="Лайки", blank=True, related_name="+"
    )
    dislikes = models.ManyToManyField(
        User, verbose_name="Дизлайки", blank=True, related_name="+"
    )
    text = models.TextField("Сообщение", max_length=3000)

    class Meta:
        abstract = True


class ProfileModel(MyBaseModel):
    """
    Абстрактная модель для профилей компании или специалиста.
    """

    phone = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Телефон"
    )
    country = models.CharField(
        max_length=255, blank=True, null=True, default="Россия", verbose_name="Страна"
    )
    city = models.CharField(
        max_length=255, blank=True, null=True, default="Москва", verbose_name="Город"
    )
    about = models.TextField(blank=True, null=True, verbose_name="Описание")
    slug = models.SlugField("Слаг", unique=True, blank=True, null=True)

    class Meta:
        abstract = True


class ResumeOrVacancyModel(MyBaseModel):
    """
    Абстрактная модель для резюме и вакансий.
    """

    position = models.CharField("Должность", max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )
    min_salary = models.SmallIntegerField("Минимальная зарплата", blank=True, null=True)
    max_salary = models.SmallIntegerField(
        "Максимальная зарплата", blank=True, null=True
    )
    currency = models.CharField(
        "Валюта", max_length=200, choices=CURRENCY_TYPE, default="RUB"
    )
    work_schedule = models.CharField(
        "График работы", max_length=200, choices=WORK_SCHEDULE, default="full-time"
    )
    stacks = models.ManyToManyField(Stack, verbose_name="Стек", blank=True)

    class Meta:
        abstract = True

    def clean(self):
        if self.min_salary and self.max_salary and self.min_salary > self.max_salary:
            raise ValidationError(
                "Минимальная зарплата не может быть больше максимальной"
            )
        return super().clean()
