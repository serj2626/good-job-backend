from django.contrib import admin
from .models import ResponseVacancy, Message, Interview


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    """Admin View for Interview)"""

    list_display = (
        "response_vacancy",
        "employee",
        "company",
        "status",
        "created_at",
        "date_interview",
        "updated_at",
    )


@admin.register(ResponseVacancy)
class ResponseVacancyAdmin(admin.ModelAdmin):

    list_display = (
        "vacancy",
        "resume",
        "created_at",
        "updated_at",
        "status",
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Admin View for Message)"""

    list_display = (
        "response_vacancy",
        "sender",
        "receiver",
        "text",
        "created_at",
        "updated_at",
    )
