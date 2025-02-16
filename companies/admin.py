from django.contrib import admin
from .models import CommentCompany, Company, Vacancy, CheckCompany


class CheckCompanyInline(admin.TabularInline):
    model = CheckCompany


admin.site.register(CheckCompany)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """
    Админка компаний
    """

    inlines = [CheckCompanyInline]

    list_display = (
        "full_name",
        "user",
        "type",
        "site",
        "phone",
        "country",
        "city",
        "slug",
        "is_verified",
    )

    def full_name(self, obj):
        return f"{obj.get_type_display()} {obj.name}"

    save_on_top = True
    full_name.short_description = "Название компании"


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


@admin.register(CommentCompany)
class CommentCompanyAdmin(admin.ModelAdmin):
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
