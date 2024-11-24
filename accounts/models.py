import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone

from common.const import STATUS_FRIEND_REQUEST, USER_TYPES


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, verbose_name="Почта")
    type = models.CharField(
        max_length=255, choices=USER_TYPES, default="Employee", verbose_name="Тип"
    )
    online = models.BooleanField(default=False, verbose_name="онлайн")
    friends = models.ManyToManyField(
        "User", blank=True, symmetrical=True, verbose_name="Друзья"
    )
    is_verified = models.BooleanField(default=False, verbose_name="подтвержден")
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.get_type_display()} ({self.email})"


class FriendRequest(models.Model):
    """
    Модель заявки в друзья
    """

    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="from_user"
    )
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to_user")
    status = models.CharField(
        max_length=255, choices=STATUS_FRIEND_REQUEST, default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Заявка в друзья"
        verbose_name_plural = "Заявки в друзья"

    def __str__(self):
        return f"Заявка в друзья {self.from_user} -> {self.to_user}"


class Message(models.Model):
    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="from_user_messages",
        verbose_name="Отправитель",
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="to_user_messages",
        verbose_name="Получатель",
    )
    content = models.TextField("Сообщение", max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
