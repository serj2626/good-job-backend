from django.contrib import admin
from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """
    Админка уведомлений компаний
    """

    list_display = (
        "message",
        "created_at",
        "type",
        "read",
    )
