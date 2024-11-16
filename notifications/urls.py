from django.urls import path
from .views import (
    NotificationCompanyView,
    NotificationEmployeeView,
    NotificationCompanyDetailView,
    NotificationEmployeeDetailView,
)


urlpatterns = [
    path("employee/", NotificationEmployeeView.as_view(), name="notification-employee"),
    path(
        "employee/<int:notification_id>/",
        NotificationEmployeeDetailView.as_view(),
        name="notification-employee-detail",
    ),
    path("company/", NotificationCompanyView.as_view(), name="notification-company"),
    path(
        "company/<int:notification_id>/",
        NotificationCompanyDetailView.as_view(),
        name="notification-company-detail",
    ),
]
