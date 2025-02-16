from django.urls import path
from .views import NotificationView, NotificationDetailView


urlpatterns = [
    path("", NotificationView.as_view(), name="notifications"),
    path("<int:pk>/", NotificationDetailView.as_view(), name="notification-detail"),
]
