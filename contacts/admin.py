from django.contrib import admin
from .models import Feedback, Subscription


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """
    Админка обратной связи
    """

    list_display = (
        "user",
        "subject",
        "text",
        "photo",
        "created_at",
    )


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """
    Админка подписок
    """

    list_display = (
        "email",
        "created_at",
    )
