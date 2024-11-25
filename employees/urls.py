from django.urls import path

from .views import (
    EmployeeDetailView,
    EmployeeListView,
    ExperienceListView,
    ResumeDetailView,
    ResumeListView,
    ProjectDetailView,
    ProjectListView,
)

urlpatterns = [
    path("", EmployeeListView.as_view(), name="employee-list"),
    path("<int:pk>/", EmployeeDetailView.as_view(), name="employee-detail"),
    path("experience/", ExperienceListView.as_view(), name="experience"),
    path("resume/", ResumeListView.as_view(), name="resume-list"),
    path("resume/<pk>/", ResumeDetailView.as_view(), name="resume-detail"),
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
]
