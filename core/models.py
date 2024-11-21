from django.db import models
from django.contrib.auth import get_user_model
from common.const import (
    CATEGORY_TYPES,
)

User = get_user_model()


class Category(models.Model):
    """Модель категории."""

    name = models.CharField("Название", max_length=200, choices=CATEGORY_TYPES)
    slug = models.SlugField("Slug", unique=True, blank=True, null=True)

    def clean(self):
        if not self.slug:
            self.slug = self.name.lower().replace(" ", "-")
        return super().clean()

    class Meta:
        verbose_name = " Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"Категория {self.name}"


class Stack(models.Model):
    """Модель стека."""

    name = models.CharField("Название", max_length=200)
    slug = models.SlugField("Slug", unique=True, blank=True, null=True)

    def clean(self):
        if not self.slug:
            self.slug = self.name.lower().replace(" ", "-")
        return super().clean()

    class Meta:
        verbose_name = " Стек"
        verbose_name_plural = "Стеки"

    def __str__(self):
        return f"{self.name}"


