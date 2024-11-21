from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from core.models import Category, Stack
from common.models import ProfileModel, ResumeOrVacancyModel
from common.service import (
    get_path_for_avatar,
    get_path_for_image_project,
)

User = get_user_model()


class Employee(ProfileModel):
    """Модель работника."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    first_name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Фамилия"
    )
    middle_name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Отчество"
    )
    date_of_birth = models.DateField(
        blank=True, null=True, verbose_name="Дата рождения"
    )

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"

    def __str__(self):
        return f"Работник {self.first_name} {self.last_name}"


class Project(models.Model):
    """Модель проекта."""

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, verbose_name="Работник"
    )
    title = models.CharField("Название проекта", max_length=300)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория"
    )
    image = models.ImageField(
        "Постер", upload_to=get_path_for_image_project, blank=True, null=True
    )
    likes = models.ManyToManyField(User, verbose_name="Лайки", blank=True)
    stacks = models.ManyToManyField(Stack, verbose_name="Стек", blank=True)
    link = models.URLField("Ссылка на проект", blank=True, null=True)
    description = models.TextField("Описание", max_length=3000, blank=True, null=True)
    created_at = models.DateTimeField("Создан", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return f"Проект {self.title} работника {self.employee}"


class Experience(models.Model):
    """Модель опыта работы."""

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, verbose_name="Работник"
    )
    company = models.CharField("Компания", max_length=300)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория"
    )
    stacks = models.ManyToManyField(Stack, verbose_name="Стек")
    position = models.CharField("Должность", max_length=200)
    requirements = models.TextField(
        "Требования", max_length=3000, blank=True, null=True
    )
    description = models.TextField("Описание", max_length=3500, blank=True, null=True)
    start_date = models.DateField("Начало работы")
    end_date = models.DateField("Окончание работы", blank=True, null=True)

    def clean(self):
        if self.end_date <= self.start_date:
            raise ValidationError(
                "Дата окончания работы не может быть раньше даты начала работы"
            )
        return super().clean()

    class Meta:
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"

    def __str__(self):
        return f"Опыт работы {self.employee} в {self.company}"


class Resume(ResumeOrVacancyModel):
    """Модель резюме."""

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, verbose_name="Работник"
    )
    avatar = models.ImageField(
        "Аватар", upload_to=get_path_for_avatar, blank=True, null=True
    )
    experience = models.ManyToManyField(
        Experience, verbose_name="Опыт работы", blank=True
    )
    about = models.TextField("О себе", max_length=1000, blank=True, null=True)
    visibility = models.BooleanField("Видимость", default=True)

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"

    def __str__(self):
        return f"Резюме от {self.employee}"
