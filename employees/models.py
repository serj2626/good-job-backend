from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from common.const import STATUS_EMPLOYEE, TYPE_EDUCATION, TYPE_GENDER, TYPE_SOCIAL_LINK
from core.models import Category, Stack
from common.models import (
    CommentBaseModel,
    EducationOrExperienceModel,
    ProfileModel,
    ResumeOrVacancyModel,
    MyBaseModel,
)
from common.service import (
    get_clear_slug,
    get_path_for_avatar_resume,
    get_path_for_avatar_employee,
    get_path_for_image_project,
)
from django.utils.timesince import timesince

User = get_user_model()


class Employee(ProfileModel):
    """Модель работника."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    status = models.CharField(
        choices=STATUS_EMPLOYEE, max_length=300, default="search", verbose_name="Статус"
    )
    position = models.CharField("Должность", max_length=300, blank=True, null=True)
    avatar = models.ImageField(
        "Аватар", upload_to=get_path_for_avatar_employee, blank=True, null=True
    )
    stacks = models.ManyToManyField(Stack, verbose_name="Стек", blank=True)
    first_name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Фамилия"
    )
    gender = models.CharField(
        max_length=255, choices=TYPE_GENDER, default="other", verbose_name="Пол"
    )
    date_of_birth = models.DateField(
        blank=True, null=True, verbose_name="Дата рождения", default=timezone.now
    )

    def clean_date_of_birth(self):
        if self.date_of_birth > timezone.now():
            raise ValidationError("Дата рождения не может быть в будущем")
        if (timezone.now() - self.date_of_birth) < 16:
            raise ValidationError("Работник должен быть старше 16 лет")
        return self.date_of_birth

    def clean(self):
        if not self.slug:
            self.slug = get_clear_slug(self.user.email)
        super().clean()

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"

    def __str__(self):
        return f"Специалист {self.first_name} {self.last_name}"


class SocialLinkEmployee(models.Model):
    """Модель социальной сети работника."""

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, verbose_name="Специалист"
    )
    name = models.CharField("Название", max_length=300, choices=TYPE_SOCIAL_LINK)
    link = models.URLField("Ссылка", blank=True, null=True)

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"

    def __str__(self):
        return f"Социальная сеть {self.name}"


class Project(MyBaseModel):
    """Модель проекта."""

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="projects",
        verbose_name="Специалист",
    )
    title = models.CharField("Название проекта", max_length=300)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория"
    )
    image = models.ImageField(
        "Постер", upload_to=get_path_for_image_project, blank=True, null=True
    )
    likes = models.ManyToManyField(
        User, verbose_name="Лайки", blank=True, related_name="+"
    )
    dislikes = models.ManyToManyField(
        User, verbose_name="Дизлайки", blank=True, related_name="+"
    )
    stacks = models.ManyToManyField(Stack, verbose_name="Стек", blank=True)
    link = models.URLField("Ссылка на проект", blank=True, null=True)
    description = models.TextField("Описание", blank=True, null=True)

    def time_ago(self):
        return timesince(self.created_at)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return f"Проект {self.title} специалиста {self.employee}"


class Experience(EducationOrExperienceModel):
    """Модель опыта работы."""

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name="Специалист",
        related_name="experiences",
    )
    company = models.CharField("Компания", max_length=300)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория"
    )
    stacks = models.ManyToManyField(Stack, verbose_name="Стек")
    position = models.CharField("Должность", max_length=200)
    description = models.TextField("Описание", blank=True, null=True)

    # def clean(self):
    #     if self.end_date and self.start_date and (self.end_date <= self.start_date):
    #         raise ValidationError(
    #             "Дата окончания работы не может быть раньше даты начала работы"
    #         )
    #     return super().clean()

    class Meta:
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"

    def __str__(self):
        return f"Опыт работы {self.employee} в {self.company}"


class Resume(ResumeOrVacancyModel):
    """Модель резюме."""

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name="Работник",
        related_name="resumes",
    )
    avatar = models.ImageField(
        "Аватар",
        upload_to=get_path_for_avatar_resume,
        default="employee/employee.jpg",
        blank=True,
        null=True,
    )
    about = models.TextField("О себе", blank=True, null=True)
    is_visible = models.BooleanField("Видимость", default=True)

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"

    def __str__(self):
        return f"Резюме от {self.employee}"


class Education(EducationOrExperienceModel):
    """Модель образования."""

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name="Работник",
        related_name="educations",
    )
    type = models.CharField(
        "Тип", max_length=300, choices=TYPE_EDUCATION, default="univer"
    )
    university = models.CharField("Университет", max_length=300)
    specialization = models.CharField("Специализация", max_length=300)

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образование"

    def __str__(self):
        return f"Образование {self.employee} в {self.university}"


class CommentProject(CommentBaseModel):
    """
    Модель комментария к проекту.
    """

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name="Проект",
        related_name="all_comments",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="comments_by_project",
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Родительский комментарий",
        blank=True,
        null=True,
    )

    def time_ago(self):
        return timesince(self.created_at)

    class Meta:
        verbose_name = "Комментарий к проекту"
        verbose_name_plural = "Комментарии к проекту"

    def __str__(self):
        return f"Комментарий к проекту {self.project}"
