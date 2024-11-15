from django.db import models

from accounts.models import User


TYPE_NOTIFICATION = (
    ("new_vacancy", "Новая вакансия"),
    ("new_interview", "Новый интервью"),
    ("new_message", "Новое сообщение"),
    ("new_response", "Новый отклик"),
    ("archive_vacancy", "Вакансия перенесена в архив"),
)


class NotificationEmployee(models.Model):
    """
    Модель уведомлений для работников
    """
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=255, choices=TYPE_NOTIFICATION)
    read = models.BooleanField(default=False, verbose_name="Прочитано")



class NotificationCompany(models.Model):
    """
    Модель уведомлений для компаний
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=255, choices=TYPE_NOTIFICATION)
    read = models.BooleanField(default=False, verbose_name="Прочитано")