from django.db import models
from accounts.models import User
from common.const import TYPE_NOTIFICATION
from common.models import MyBaseModel


class Notification(MyBaseModel):
    """
    Модель уведомлений для работников и  компании
    """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications"
    )
    message = models.TextField()
    type = models.CharField(max_length=255, choices=TYPE_NOTIFICATION)
    read = models.BooleanField(default=False, verbose_name="Прочитано")

    class Meta:
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"

    def __str__(self):
        return f"Уведомление {self.user}"
