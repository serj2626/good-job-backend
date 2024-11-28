from django.contrib import admin

from .models import Comment, Company, Vacancy


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """
    Админка компаний
    """

    list_display = (
        "user",
        "name",
        "site",
        "phone",
        "country",
        "city",
        "slug",
        "is_verified",
    )

    def is_verified(self, obj):
        return obj.user.is_verified

    is_verified.short_description = "Проверена"


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    """
    Админка вакансий
    """

    list_display = (
        "company",
        "category",
        "position",
        "level",
        "min_salary",
        "max_salary",
        "work_schedule",
        "work_experience",
        "status_vacancy",
    )
    filter_horizontal = ("stacks",)

    list_editable = (
        "level",
        "status_vacancy",
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Админка комментарий
    """

    list_display = (
        "get_text",
        "user",
        "company",
        "stars",
        "created_at",
        "updated_at",
    )

    def get_text(self, obj):
        return obj.text[:36] + "..."

    get_text.short_description = "Сообщение"
