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
    StackListView
)


urlpatterns = [
    path("category/", CategoryView.as_view(), name="category"),
    path("experience/", ExperienceListView.as_view(), name="experience"),
    path("comments/", CommentListView.as_view(), name="comments"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comments-detail"),
    path("resume-list/", ResumeListView.as_view(), name="resume-list"),
    path("resume-list/<int:pk>/", ResumeDetailView.as_view(), name="resume-detail"),
    path("vacancy-list/", VacancyListView.as_view(), name="vacancy-list"),
    path("vacancy-list/<int:pk>/", VacancyDetailView.as_view(), name="vacancy-detail"),
    path("stack-list/", StackListView.as_view(), name="stack-list"),
]
