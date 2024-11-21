from django.contrib import admin
from django.utils.html import format_html
from .models import Employee, Experience, Project, Resume, SocialLinkEmployee


@admin.register(SocialLinkEmployee)
class SocialLinkEmployeeAdmin(admin.ModelAdmin):
    """
    Админка социальных сетей работников
    """

    list_display = ("employee", "name", "link")


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """
    Админка работников
    """

    list_display = (
        "user",
        "position",
        "last_name",
        "first_name",
        "middle_name",
        "date_of_birth",
        "phone",
        "country",
        "city",
        "slug",
        "get_avatar",
    )
    # list_editable = (
    #     "first_name",
    #     "last_name",
    #     "middle_name",
    # )

    def get_avatar(self, obj):
        return format_html(
            '<img src="{}" width="50" style="border-radius: 50px" height="50" />'.format(obj.avatar.url)
        )

    get_avatar.short_description = "Аватар"


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

    filter_horizontal = ("stacks", )
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
