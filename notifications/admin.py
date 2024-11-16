from django.contrib import admin
from .models import NotificationCompany, NotificationEmployee


@admin.register(NotificationCompany)
class NotificationCompanyAdmin(admin.ModelAdmin):
    """
    Админка уведомлений компаний
    """

    list_display = (
        "user",
        "message",
        "created_at",
        "type",
        "read",
    )


@admin.register(NotificationEmployee)
class NotificationEmployeeAdmin(admin.ModelAdmin):
    """
    Админка уведомлений работников
    """

    list_display = (
        "user",
        "message",
        "created_at",
        "type",
        "read",
    )
