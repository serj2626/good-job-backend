from django.urls import path

from .views import (
    EmployeeDetailView,
    EmployeeListView,
    ExperienceListView,
    ResumeDetailView,
    ResumeListView,
)

urlpatterns = [
    path("", EmployeeListView.as_view(), name="employee-list"),
    path("<int:pk>/", EmployeeDetailView.as_view(), name="employee-detail"),
    path("experience/", ExperienceListView.as_view(), name="experience"),
    path("resume/", ResumeListView.as_view(), name="resume-list"),
    path("resume/<int:pk>/", ResumeDetailView.as_view(), name="resume-detail"),
]
