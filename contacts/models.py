from re import sub
from django.db import models
from django.contrib.auth import get_user_model

from .service import get_path_for_photo_feedback


User = get_user_model()


class Subscription(models.Model):
    """Модель подписки."""

    email = models.EmailField("Почта", max_length=254, unique=True)
    created_at = models.DateTimeField("Создан", auto_now_add=True)

    def __str__(self):
        return f"Подписка на новости  от {self.email}"

    class Meta:

        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"




class Feedback(models.Model):
    """Модель обратной связи."""

    TYPE_SUBJECT = (
        ("question", "Вопрос"),
        ("suggestion", "Предложение"),
        ("complaint", "Жалоба"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        blank=True,
        null=True,
    )
    subject = models.CharField(
        "Тема", max_length=200, choices=TYPE_SUBJECT, default="question"
    )
    text = models.TextField("Сообщение", max_length=1000)
    photo = models.ImageField(
        "Фото", upload_to=get_path_for_photo_feedback, blank=True, null=True
    )
    created_at = models.DateTimeField("Создан", auto_now_add=True)

    def __str__(self):
        return f"Обратная связь от {self.user.name}"

    class Meta:

        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"
