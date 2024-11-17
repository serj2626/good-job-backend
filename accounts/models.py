import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone

from common.const import USER_TYPES

from .service import get_clear_slug, get_path_for_avatar


class CustomUserManager(UserManager):
    def _create_user(self, name, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(name, email, password, **extra_fields)

    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(name, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, verbose_name="Почта")
    name = models.CharField(
        max_length=255, blank=True, null=True, default="", verbose_name="Имя"
    )
    type = models.CharField(
        max_length=255, choices=USER_TYPES, default="Employee", verbose_name="Тип"
    )

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
        ordering = ["name"]

    def __str__(self):
        return f"{self.get_type_display()} ({self.name})"


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    country = models.CharField(
        max_length=255, blank=True, null=True, default="Россия", verbose_name="Страна"
    )
    city = models.CharField(
        max_length=255, blank=True, null=True, default="Москва", verbose_name="Город"
    )
    avatar = models.ImageField(
        upload_to=get_path_for_avatar, blank=True, null=True, verbose_name="Аватар"
    )
    slug = models.SlugField(
        max_length=255, unique=True, blank=True, null=True, verbose_name="Слаг"
    )
    online = models.BooleanField(default=False, verbose_name="онлайн")
    link = models.URLField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Ссылка на сайт"
    )
    verified = models.BooleanField(default=False, verbose_name="Проверенный")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def clean(self):
        if not self.slug:
            self.slug = get_clear_slug(self.user.email)
        super().clean()

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return self.user.email
