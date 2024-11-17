from django.contrib import admin
from .models import User, Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Админка пользователей
    """

    list_display = (
        "email",
        "name",
        "type",
        "is_active",
        "is_superuser",
        "is_staff"
    )
    list_editable = ("type", )
    list_filter = ('type',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Админка профилей
    """

    list_display = (
        "get_name",
        "user",
        "country",
        "city",
        "link",
        "avatar",
        "slug",
        "online",
        "verified"
    )

    list_editable = ("country", "city",)

    def get_name(self, obj):
        return obj.user.name

    get_name.short_description = "Работник | Компания"
