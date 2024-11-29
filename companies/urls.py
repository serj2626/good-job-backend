from django.urls import path

from .views import (
    CommentDetailView,
    CommentListView,
    CompanyDetailView,
    CompanyListView,
    VacancyDetailView,
    VacancyListView,
)

urlpatterns = [
    path("", CompanyListView.as_view(), name="company-list"),
    path("<int:pk>/", CompanyDetailView.as_view(), name="company-detail"),
    path("comments/", CommentListView.as_view(), name="comments"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comments-detail"),
    path("vacancy/", VacancyListView.as_view(), name="vacancy-list"),
    path("vacancy/<pk>/", VacancyDetailView.as_view(), name="vacancy-detail"),
]
