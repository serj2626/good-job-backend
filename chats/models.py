import uuid
from django.contrib.auth import get_user_model
from django.db import models
from core.models import Vacancy, Resume
from django.utils.timesince import timesince


User = get_user_model()


class ResponseVacancy(models.Model):
    """Модель отклика на вакансию"""

    STATUS_RESPONSE = (
        ("new", "Новый"),
        ("accepted", "Принят"),
        ("interview", "Интервью"),
        ("offered", "Предложение на работу"),
        ("rejected", "Отклонен"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Вакансия",
        related_name="all_responses",
    )
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        verbose_name="Резюме",
        related_name="my_responses",
    )
    created_at = models.DateTimeField("Создан", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлен", auto_now=True)
    status = models.CharField(
        "Статус", max_length=200, choices=STATUS_RESPONSE, default="new"
    )

    def created_at_formatted(self):
        return timesince(self.created_at)

    class Meta:
        verbose_name = "Отклик"
        verbose_name_plural = "Отклики"

    def __str__(self):
        return f"Отклик на вакансию от {self.resume.employee.email}"


class Message(models.Model):
    """Модель сообщения в отклике на вакансию"""

    response_vacancy = models.ForeignKey(
        ResponseVacancy,
        on_delete=models.CASCADE,
        verbose_name="Отклик",
        related_name="all_messages",
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Отправитель",
        related_name="my_messages",
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Получатель",
        related_name="response_vacancy_messages",
    )
    text = models.TextField("Текст сообщения", max_length=1500)
    created_at = models.DateTimeField("Создан", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлен", auto_now=True)

    def created_at_formatted(self):
        return timesince(self.created_at)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return f"Сообщение от {self.response_vacancy.resume.employee.email}"


class Interview(models.Model):
    """Модель интервью"""

    STATUS_INTERVIEW = (
        ("new", "Создан"),
        ("finished", "Окончен"),
        ("canceled", "Отменен"),
        ("accepted", "Успешен"),
        ("rejected", "Отклонен"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    response_vacancy = models.ForeignKey(
        ResponseVacancy,
        on_delete=models.CASCADE,
        verbose_name="Отклик",
        related_name="all_interviews",
    )
    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Работник",
        related_name="my_interviews",
    )
    company = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Компания",
        related_name="interviews",
    )
    status = models.CharField(
        "Статус", max_length=200, choices=STATUS_INTERVIEW, default="new"
    )
    created_at = models.DateTimeField("Создан", auto_now_add=True)
    date_interview = models.DateTimeField("Дата интервью", blank=True, null=True)
    updated_at = models.DateTimeField("Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Интервью"
        verbose_name_plural = "Интервью"

    def __str__(self):
        return f"Интервью для {self.employee.email}"
