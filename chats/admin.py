from django.contrib import admin
from .models import ResponseVacancy, Message, Interview


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


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
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
