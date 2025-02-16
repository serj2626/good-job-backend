import uuid
from django.contrib.auth import get_user_model
from django.db import models
from employees.models import Employee, Resume
from companies.models import Company, Vacancy
from common.const import STATUS_INTERVIEW, STATUS_RESPONSES
from common.models import MyBaseModel
from django.utils.timesince import timesince


User = get_user_model()


class ResponseVacancy(MyBaseModel):
    """Модель отклика на вакансию"""

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
        related_name="all_responses",
    )

    status = models.CharField(
        "Статус", max_length=200, choices=STATUS_RESPONSES, default="new"
    )

    def time_ago(self):
        return timesince(self.created_at)

    class Meta:
        verbose_name = "Отклик"
        verbose_name_plural = "Отклики"

    def __str__(self):
        return f"Отклик на вакансию от {self.resume.employee}"


class ResponseLetter(MyBaseModel):
    """Модель сопроводительного письма"""

    response_vacancy = models.ForeignKey(
        ResponseVacancy,
        on_delete=models.CASCADE,
        verbose_name="Отклик",
        related_name="all_letters",
    )
    text = models.TextField("Текст письма", max_length=5000)

    class Meta:
        verbose_name = "Сопроводительное письмо"
        verbose_name_plural = "Сопроводительные письма"

    def __str__(self):
        return f"Сопроводительное письмо от {self.response_vacancy.resume.employee}"


class MessageToResponse(MyBaseModel):
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

    def time_ago(self):
        return timesince(self.created_at)

    class Meta:
        verbose_name = "Сообщение отклика"
        verbose_name_plural = "Сообщения отклика"

    def __str__(self):
        return f"Сообщение от {self.response_vacancy.resume.employee.user}"


class Interview(MyBaseModel):
    """Модель интервью"""


    response_vacancy = models.ForeignKey(
        ResponseVacancy,
        on_delete=models.CASCADE,
        verbose_name="Отклик",
        related_name="all_interviews",
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name="Работник",
        related_name="my_interviews",
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name="Компания",
        related_name="interviews",
    )
    status = models.CharField(
        "Статус", max_length=200, choices=STATUS_INTERVIEW, default="new"
    )
    date_interview = models.DateTimeField("Дата интервью", blank=True, null=True)


    class Meta:
        verbose_name = "Интервью"
        verbose_name_plural = "Интервью"

    def __str__(self):
        return f"Интервью для {self.employee}"
