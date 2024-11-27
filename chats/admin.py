from django.contrib import admin
from .models import ResponseVacancy, MessageToResponse, Interview, ResponseLetter


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    """
    Админка интервью
    """

    list_display = (
        "response_vacancy",
        "employee",
        "company",
        "status",
        "date_interview",
    )
    list_editable = ("status",)

    list_display_links = (
        "response_vacancy",
        "employee",
        "company",
    )


@admin.register(ResponseVacancy)
class ResponseVacancyAdmin(admin.ModelAdmin):
    """
    Админка откликов на вакансию
    """

    list_display = (
        "vacancy",
        "resume",
        "status",
    )

    list_editable = ("status",)

    list_display_links = (
        "vacancy",
        "resume",
    )


@admin.register(MessageToResponse)
class MessageToResponseAdmin(admin.ModelAdmin):
    """
    Админка сообщений
    """

    list_display = (
        "response_vacancy",
        "sender",
        "receiver",
        "get_msg",
    )

    def get_msg(self, obj):
        return str(obj.text)[0:36] + "..."

    get_msg.short_description = "Сообщение"


@admin.register(ResponseLetter)
class ResponseLetterAdmin(admin.ModelAdmin):
    """
    Админка сопроводительных писем
    """

    list_display = (
        "response_vacancy",
        "get_employee",
        "get_company",
        "get_text",
    )

    def get_text(self, obj):
        return str(obj.text)[0:36] + "..."

    def get_employee(self, obj):
        return obj.response_vacancy.resume.employee

    def get_company(self, obj):
        return obj.response_vacancy.resume.company

    get_company.short_description = "Компания"
    get_employee.short_description = "Специалист"
    get_text.short_description = "Текст письма"
