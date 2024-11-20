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
    Employee,
    Company,
    Projects,
)


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    """
    Админка проектов
    """

    list_display = (
        "employee",
        "title",
        "category",
        "link",
        "get_description",
    )

    def get_description(self, obj):
        return obj.description[:36] + "..."

    get_description.short_description = "Описание"


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
    )
    list_editable = ("name", "site", "phone", "country", "city")


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """
    Админка работников
    """

    list_display = (
        "user",
        "last_name",
        "first_name",
        "middle_name",
        "date_of_birth",
        "phone",
        "country",
        "city",
        "slug",
    )
    list_editable = (
        "first_name",
        "last_name",
        "middle_name",
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
        "position",
        "work_schedule",
        "min_salary",
        "max_salary",
    )
    list_editable = ("min_salary", "max_salary", "work_schedule")

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
        "position",
        "level",
        "min_salary",
        "max_salary",
        "work_schedule",
        "work_experience",
        "status_vacancy",
    )

    list_editable = (
        "level",
        "status_vacancy",
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    """
    Админка опыта работы
    """

    list_display = (
        "employee",
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
