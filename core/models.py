from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from common.models import ProfileModel, ResumeOrVacancyModel
from common.service import get_clear_slug, get_path_for_avatar, get_path_for_image_project
from common.const import (
    CATEGORY_TYPES,
    LEVELS_REQUIREMENTS,
    STATUS_VACANCY,
)

User = get_user_model()


class Category(models.Model):
    """Модель категории."""

    name = models.CharField("Название", max_length=200, choices=CATEGORY_TYPES)
    slug = models.SlugField("Slug", unique=True, blank=True, null=True)

    def clean(self):
        if not self.slug:
            self.slug = self.name.lower().replace(" ", "-")
        return super().clean()

    class Meta:
        verbose_name = " Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"Категория {self.name}"


class Stack(models.Model):
    """Модель стека."""

    name = models.CharField("Название", max_length=200)
    slug = models.SlugField("Slug", unique=True, blank=True, null=True)

    def clean(self):
        if not self.slug:
            self.slug = self.name.lower().replace(" ", "-")
        return super().clean()

    class Meta:
        verbose_name = " Стек"
        verbose_name_plural = "Стеки"

    def __str__(self):
        return f"{self.name}"


class Employee(ProfileModel):
    """Модель работодателя."""

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


class Company(ProfileModel):
    """Модель компании."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    name = models.CharField("Название компании", max_length=500, blank=True, null=True)
    site = models.URLField("Сайт компании", blank=True, null=True)

    def clean(self):
        if not self.slug:
            self.slug = get_clear_slug(self.user.email)
        super().clean()

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return f"Компания {self.name}"


class Projects(models.Model):
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
    about = models.TextField("Описание", max_length=3500, blank=True, null=True)
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

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"

    def __str__(self):
        return f"Резюме от {self.employee}"


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
    about = models.TextField("Описание", max_length=3500, blank=True, null=True)

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return f"Вакансия от {self.category.name}"


class Comment(models.Model):
    """Модель комментария."""

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
    text = models.TextField("Сообщение", max_length=3000)
    stars = models.SmallIntegerField(
        "Оценка",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    created_at = models.DateTimeField("Создан", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"Комментарий от {self.user.email}"


class FavoriteResume(models.Model):
    """
    Модель избранных резюме  для компании.
    """

    resume = models.ForeignKey(
        Resume, on_delete=models.SET_NULL, null=True, verbose_name="Резюме"
    )
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, verbose_name="Компания"
    )
    created_at = models.DateTimeField("Создан", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлен", auto_now=True)

    def __str__(self):
        return f"Избранное резюме {self.resume} для компании {self.company}"

    class Meta:
        verbose_name = "Избранные резюме"
        verbose_name_plural = "Избранные резюме"


class FavoriteVacancy(models.Model):
    """
    Модель избранных вакансий для работника.
    """

    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.SET_NULL, null=True, verbose_name="Вакансия"
    )
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, verbose_name="Работник"
    )
    created_at = models.DateTimeField("Создан", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлен", auto_now=True)

    def __str__(self):
        return f"Избранная вакансия {self.vacancy} для работника {self.employee}"

    class Meta:
        verbose_name = "Избранные вакансии"
        verbose_name_plural = "Избранные вакансии"
