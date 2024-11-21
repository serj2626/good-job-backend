from django.urls import path

from .views import (
    FavoriteResumeDetailView,
    FavoriteResumeListView,
    FavoriteVacancyDetailView,
    FavoriteVacancyListView,
)


urlpatterns = [
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
]
