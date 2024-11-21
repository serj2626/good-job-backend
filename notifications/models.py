from django.db import models
from companies.models import Company
from employees.models import Employee
from common.const import TYPE_NOTIFICATION


class NotificationEmployee(models.Model):
    """
    Модель уведомлений для работников
    """

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=255, choices=TYPE_NOTIFICATION)
    read = models.BooleanField(default=False, verbose_name="Прочитано")

    class Meta:
        verbose_name = "Уведомление работника"
        verbose_name_plural = "Уведомления работников"

    def __str__(self):
        return f"Уведомление работника {self.user.name}"


class NotificationCompany(models.Model):
    """
    Модель уведомлений для компаний
    """

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=255, choices=TYPE_NOTIFICATION)
    read = models.BooleanField(default=False, verbose_name="Прочитано")

    class Meta:
        verbose_name = "Уведомление компании"
        verbose_name_plural = "Уведомления компаний"

    def __str__(self):
        return f"Уведомление компании {self.user.name}"
