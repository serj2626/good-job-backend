from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from common.service import get_path_for_avatar_company
from employees.models import Resume
from common.models import ProfileModel, ResumeOrVacancyModel
from common.const import (
    LEVELS_REQUIREMENTS,
    STATUS_VACANCY,
)
from django.utils.timesince import timesince


User = get_user_model()


class Company(ProfileModel):
    """Модель компании."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    avatar = models.ImageField(
        "Аватар", upload_to=get_path_for_avatar_company, blank=True, null=True
    )
    name = models.CharField("Название компании", max_length=500, blank=True, null=True)
    site = models.URLField("Сайт компании", blank=True, null=True)

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return f"Компания {self.name}"


class Vacancy(ResumeOrVacancyModel):
    """Модель вакансии."""

    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, verbose_name="Компания"
    )
    level = models.CharField(
        "Уровень", max_length=200, choices=LEVELS_REQUIREMENTS, default="junior"
    )
    status_vacancy = models.CharField(
        "Статус вакансии", max_length=200, choices=STATUS_VACANCY, default="open"
    )
    work_experience = models.SmallIntegerField("Стаж", blank=True, null=True)
    requirements = models.TextField(
        "Требования", max_length=3000, blank=True, null=True
    )
    description = models.TextField("Описание", max_length=3500, blank=True, null=True)

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return f"Вакансия от {self.category.name}"


class Comment(models.Model):
    """Модель комментария к компании."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="my_comments",
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name="Компания",
        related_name="all_comments",
    )
    likes = models.ManyToManyField(User, verbose_name="Лайки", blank=True)
    text = models.TextField("Сообщение", max_length=3000)
    stars = models.SmallIntegerField(
        "Оценка",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    created_at = models.DateTimeField("Создан", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлен", auto_now=True)

    def time_ago(self):
        return timesince(self.created_at)

    class Meta:
        verbose_name = "Комментарий к компании"
        verbose_name_plural = "Комментарии к компании"

    def __str__(self):
        return f"Комментарий от {self.user.email}"
