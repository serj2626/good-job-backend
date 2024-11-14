from django.contrib import admin
from .models import Feedback, Subscription


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """Admin View for Feedback"""

    list_display = (
        "user",
        "subject",
        "text",
        "photo",
        "created_at",
    )


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """Admin View for Subscription"""

    list_display = (
        "email",
        "created_at",
    )
