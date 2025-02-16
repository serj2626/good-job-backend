from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Employee,
    Experience,
    Project,
    Resume,
    SocialLinkEmployee,
    Education,
    CommentProject,
)


@admin.register(CommentProject)
class CommentProjectAdmin(admin.ModelAdmin):
    """
    Админка комментариев к проекту
    """

    list_display = (
        "project",
        "user",
        "get_text",
        "get_likes",
        "get_dislikes",
    )

    def get_text(self, obj):
        return obj.text[:36] + "..."

    def get_likes(self, obj):
        return obj.likes.count()

    def get_dislikes(self, obj):
        return obj.dislikes.count()

    get_likes.short_description = "Лайки"
    get_dislikes.short_description = "Дизлайки"
    get_text.short_description = "Текст комментария"


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    """
    Админка образования
    """

    list_display = (
        "employee",
        "type",
        "university",
        "specialization",
    )


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
        "gender",
        "date_of_birth",
        "phone",
        "country",
        "city",
        "slug",
    )

    filter_horizontal = ("stacks",)
    save_on_top = True

    def get_avatar(self, obj):
        return format_html(
            '<img src="{}" width="50" style="border-radius: 50px" height="50" />'.format(
                obj.avatar.url
            )
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
        "is_visible",
    )
    list_editable = ("min_salary", "max_salary", "work_schedule", "is_visible")

    filter_horizontal = ("stacks",)
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
        "category",
    )

    filter_horizontal = ("stacks",)
