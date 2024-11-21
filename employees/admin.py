from django.contrib import admin

from .models import Employee, Experience, Project, Resume


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


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
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
        "visibility",
    )
    list_editable = ("min_salary", "max_salary", "work_schedule", "visibility")

    filter_horizontal = ("stacks", "experience")
    save_on_top = True


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
