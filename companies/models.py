from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from common.service import (
    get_clear_slug,
    get_path_for_avatar_company,
    get_path_for_check_company_certificate,
    get_path_for_check_company_certificate_nalog,
    get_path_for_check_company_constitution,
    get_path_for_check_company_egrul,
    get_path_for_check_company_license,
    get_path_for_check_company_no_debt,
)
from employees.models import Resume
from common.models import ProfileModel, ResumeOrVacancyModel
from common.const import (
    COMPANY_TYPES,
    LEVELS_REQUIREMENTS,
    STATUS_CHECK_COMPANY,
    STATUS_VACANCY,
)
from django.utils.timesince import timesince


User = get_user_model()


class Company(ProfileModel):
    """Модель компании."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    type = models.CharField(
        "Тип компании", choices=COMPANY_TYPES, max_length=30, default="OOO"
    )
    avatar = models.ImageField(
        "Аватар",
        upload_to=get_path_for_avatar_company,
        default="company/company.jpg",
        blank=True,
        null=True,
    )
    count_employees = models.SmallIntegerField("Количество  сотрудников", default=0)
    name = models.CharField("Название компании", max_length=500, blank=True, null=True)
    site = models.URLField("Сайт компании", blank=True, null=True)
    is_verified = models.BooleanField("Проверенная компания", default=False, blank=True)

    def clean(self):
        if not self.slug:
            self.slug = get_clear_slug(self.user.email)
        super().clean()

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return f"{self.get_type_display()} {self.name}"


class CheckCompany(models.Model):
    """
    Модель проверки компании.
    """

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name="Компания",
        related_name="checks",
    )

    egrul = models.FileField(
        "Выписка из ЕГРЮЛ и ЕГРИП", upload_to=get_path_for_check_company_egrul
    )
    certificate = models.FileField(
        "Cвидетельство о регистрации фирмы или ИП",
        upload_to=get_path_for_check_company_certificate,
    )
    certificate_nalog = models.FileField(
        "Cправка о постановке на учет в налоговом органе",
        upload_to=get_path_for_check_company_certificate_nalog,
    )
    constitution = models.FileField(
        "Устав",
        upload_to=get_path_for_check_company_constitution,
        blank=True,
        null=True,
    )
    license = models.FileField(
        "Лицензия на необходимые виды деятельности",
        upload_to=get_path_for_check_company_license,
    )
    no_debt = models.FileField(
        "Справка, подтверждающая отсутствие налоговых задолженностей",
        upload_to=get_path_for_check_company_no_debt,
    )
    consent = models.BooleanField(
        default=False, verbose_name="Согласие на обработку персональных данных"
    )

    status = models.CharField(
        "Статус проверки",
        max_length=200,
        choices=STATUS_CHECK_COMPANY,
        default="pending",
    )

    created_at = models.DateTimeField("Создан", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлен", auto_now=True)

    def save(self, *args, **kwargs):
        if not self.consent:
            raise ValueError("Вы не согласились с обработкой персональных данных")
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Проверка компании"
        verbose_name_plural = "Проверки компании"

    def __str__(self):
        return (
            f"Проверка компании  {self.company.get_type_display()} {self.company.name}"
        )


class Vacancy(ResumeOrVacancyModel):
    """Модель вакансии."""

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name="Компания",
        related_name="vacancies",
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
    city = models.CharField("Город", max_length=200, blank=True, null=True)
    country = models.CharField("Страна", max_length=200, blank=True, null=True)
    metro = models.CharField("Станция метро", max_length=200, blank=True, null=True)
    description = models.TextField("Описание", blank=True, null=True)

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
        "Оценка", validators=[MinValueValidator(1), MaxValueValidator(5)], default=5
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
