from django.urls import path
from .views import (
    CategoryView,
    ExperienceListView,
    CommentDetailView,
    CommentListView,
    ResumeDetailView,
    ResumeListView,
    VacancyDetailView,
    VacancyListView,
    StackListView,
    FavoriteResumeListView,
    FavoriteResumeDetailView,
    FavoriteVacancyListView,
    FavoriteVacancyDetailView,
    EmployeeDetailView,
    EmployeeListView,
    CompanyDetailView,
    CompanyListView,
)


urlpatterns = [
    path("category/", CategoryView.as_view(), name="category"),
    path("company-list/", CompanyListView.as_view(), name="company-list"),
    path("company-list/<int:pk>/", CompanyDetailView.as_view(), name="company-detail"),
    path("employee-list/", EmployeeListView.as_view(), name="employee-list"),
    path(
        "employee-list/<int:pk>/", EmployeeDetailView.as_view(), name="employee-detail"
    ),
    path("experience/", ExperienceListView.as_view(), name="experience"),
    path("comments/", CommentListView.as_view(), name="comments"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comments-detail"),
    path("resume-list/", ResumeListView.as_view(), name="resume-list"),
    path("resume-list/<int:pk>/", ResumeDetailView.as_view(), name="resume-detail"),
    path("vacancy-list/", VacancyListView.as_view(), name="vacancy-list"),
    path("vacancy-list/<int:pk>/", VacancyDetailView.as_view(), name="vacancy-detail"),
    path("stack-list/", StackListView.as_view(), name="stack-list"),
    path(
        "favorite-resume-list/",
        FavoriteResumeListView.as_view(),
        name="favorite-resume-list",
    ),
    path(
        "favorite-resume-list/<int:pk>/",
        FavoriteResumeDetailView.as_view(),
        name="favorite-resume-detail",
    ),
    path(
        "favorite-vacancy-list/",
        FavoriteVacancyListView.as_view(),
        name="favorite-vacancy-list",
    ),
    path(
        "favorite-vacancy-list/<int:pk>/",
        FavoriteVacancyDetailView.as_view(),
        name="favorite-vacancy-detail",
    ),
]
