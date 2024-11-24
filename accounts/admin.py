from django.contrib import admin
from .models import User, FriendRequest, Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """
    Админка сообщений
    """

    list_display = (
        "from_user",
        "to_user",
        "content",
        "created_at",
        "updated_at",
    )

    def get_content(self, obj):
        return str(obj.content)[0:36] + "..."

    get_content.short_description = "Сообщение"


@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    """
    Админка заявок в друзья
    """

    list_display = ("from_user", "to_user", "status", "created_at", "updated_at")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Админка пользователей
    """

    list_display = (
        "email",
        "type",
        "online",
        "is_verified",
        "is_active",
        "is_superuser",
        "is_staff",
    )
    list_editable = ("type",)
    list_filter = ("type",)
    filter_horizontal = ("friends",)
