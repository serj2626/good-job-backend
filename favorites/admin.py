from django.contrib import admin

from .models import FavoriteResume, FavoriteVacancy


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
