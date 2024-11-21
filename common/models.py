from django.db import models
import uuid
from django.core.exceptions import ValidationError
from core.models import Category, Stack
from common.const import WORK_SCHEDULE
from common.service import get_clear_slug


class ProfileModel(models.Model):
    """
    Абстрактная модель для профилей Компании и Работодателя.
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
    about = models.TextField(
        max_length=5000, blank=True, null=True, verbose_name="Описание"
    )
    slug = models.SlugField("Слаг", unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    class Meta:
        abstract = True

    def clean(self):
        if not self.slug:
            self.slug = get_clear_slug(self.user.email)
        super().clean()


class ResumeOrVacancyModel(models.Model):
    """
    Абстрактная модель для резюме и вакансий.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    position = models.CharField("Должность", max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )
    min_salary = models.SmallIntegerField("Минимальная зарплата", blank=True, null=True)
    max_salary = models.SmallIntegerField(
        "Максимальная зарплата", blank=True, null=True
    )
    work_schedule = models.CharField(
        "График работы", max_length=200, choices=WORK_SCHEDULE, default="full-time"
    )
    stacks = models.ManyToManyField(Stack, verbose_name="Стек", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    class Meta:
        abstract = True

    def clean(self):
        if not self.min_salary and self.max_salary:
            raise ValidationError("Необходимо указать минимальную зарплату")
        elif self.min_salary and self.max_salary and self.min_salary > self.max_salary:
            raise ValidationError(
                "Минимальная зарплата не может быть больше максимальной"
            )
        return super().clean()
