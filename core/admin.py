from django.contrib import admin
from .models import Category, Resume, Vacancy, Experience, Comment, Stack


@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):

    list_display = ("name", "slug")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        "get_text",
        "user",
        "company",
        "stars",
        "created_at",
        "updated_at",
    )

    def get_text(self, obj):
        return obj.text[:36]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin View for Category"""

    list_display = (
        "name",
        "slug",
    )


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    """Admin View for Resume)"""

    list_display = (
        "employee",
        "category",
        "title",
        "work_schedule",
        "min_salary",
        "max_salary",
        "about",
    )


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    """Admin View for Vacancy)"""

    list_display = (
        "company",
        "category",
        "title",
        "min_salary",
        "max_salary",
        "work_schedule",
        "work_experience",
        "about",
        "status_vacancy",
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "company",
        "position",
        "requirements",
        "start_date",
        "end_date",
        "category",
    )
