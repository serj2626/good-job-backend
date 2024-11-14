from django.db import models
from accounts.models import Profile, User
import uuid
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

User = get_user_model()

Work_Schedule = (
    ("full-time", "Полный рабочий день"),
    ("part-time", "Частичная занятость"),
    ("remote", "Удаленная работа"),
)


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


class Category(models.Model):
    """Модель категории."""

    CATEGORY_TYPES = (
        ("backend", "Бэкенд"),
        ("frontend", "Фронтенд"),
        ("fullstack", "Фулстайк"),
        ("analytics", "Аналитика"),
        ("devops", "DevOps"),
        ("design", "Дизайн"),
        ("other", "Другое"),
    )
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


class Experience(models.Model):
    """Модель опыта работы."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Работник")
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
        return f"Опыт работы в {self.company}"


class Resume(models.Model):
    """Модель резюме."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Работник"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )
    title = models.CharField("Желаемая должность", max_length=200)
    work_schedule = models.CharField(
        "График работы", max_length=200, choices=Work_Schedule, default="full-time"
    )
    stacks = models.ManyToManyField(Stack, verbose_name="Стек")
    min_salary = models.SmallIntegerField("Минимальная зарплата", blank=True, null=True)
    max_salary = models.SmallIntegerField(
        "Максимальная зарплата", blank=True, null=True
    )
    experience = models.ManyToManyField(Experience, verbose_name="Опыт работы")
    about = models.TextField("О себе", max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField("Создан", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлен", auto_now=True)

    def clean(self):
        if not self.max_salary:
            self.min_salary = None
        elif self.min_salary and self.max_salary and self.min_salary > self.max_salary:
            raise ValidationError(
                "Минимальная зарплата не может быть больше максимальной"
            )
        return super().clean()

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"

    def __str__(self):
        return f"Резюме от {self.employee.email}"


class Vacancy(models.Model):
    """Модель вакансии."""

    STATUS_VACANCY = (
        ("open", " Открыта"),
        ("archived", "Архив"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )
    company = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Компания")
    title = models.CharField("Должность", max_length=200)
    work_schedule = models.CharField(
        "График работы", max_length=200, choices=Work_Schedule, default="full-time"
    )
    min_salary = models.SmallIntegerField("Минимальная зарплата", blank=True, null=True)
    max_salary = models.SmallIntegerField(
        "Максимальная зарплата", blank=True, null=True
    )
    status_vacancy = models.CharField(
        "Статус вакансии", max_length=200, choices=STATUS_VACANCY, default="open"
    )
    work_experience = models.SmallIntegerField("Стаж", blank=True, null=True)
    stacks = models.ManyToManyField(Stack, verbose_name="Стек")
    requirements = models.TextField(
        "Требования", max_length=3000, blank=True, null=True
    )
    about = models.TextField("Описание", max_length=3500, blank=True, null=True)
    created_at = models.DateTimeField("Создан", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлен", auto_now=True)

    def clean(self):
        if not self.max_salary:
            self.min_salary = None
        elif self.min_salary and self.max_salary and self.min_salary > self.max_salary:
            raise ValidationError(
                "Минимальная зарплата не может быть больше максимальной"
            )
        return super().clean()

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
        User,
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
