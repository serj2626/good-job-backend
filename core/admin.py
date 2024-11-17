from django.contrib import admin
from .models import (
    Category,
    Resume,
    Vacancy,
    Experience,
    Comment,
    Stack,
    FavoriteResume,
    FavoriteVacancy,
)


@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    """
    Админка стеков
    """

    list_display = ("name", "slug")


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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Админка категорий
    """

    list_display = (
        "name",
        "slug",
    )


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    """
    Админка резюме
    """

    list_display = (
        "employee",
        "category",
        "title",
        "work_schedule",
        "min_salary",
        "max_salary",
        "about",
    )
    filter_horizontal = ("stacks", "experience")
    save_on_top = True


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    """
    Админка вакансий
    """

    list_display = (
        "company",
        "category",
        "title",
        "level",
        "min_salary",
        "max_salary",
        "work_schedule",
        "work_experience",
        "about",
        "status_vacancy",
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    """
    Админка опыта работы
    """

    list_display = (
        "user",
        "company",
        "position",
        "requirements",
        "start_date",
        "end_date",
        "category",
    )


@admin.register(FavoriteResume)
class FavoriteResumeAdmin(admin.ModelAdmin):
    """
    Админка избранных резюме
    """

    list_display = (
        "resume",
        "company",
        "created_at",
        "updated_at",
    )


@admin.register(FavoriteVacancy)
class FavoriteVacancyAdmin(admin.ModelAdmin):
    """
    Админка избранных вакансий
    """

    list_display = (
        "vacancy",
        "employee",
        "created_at",
        "updated_at",
    )
