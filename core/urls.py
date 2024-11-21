from django.urls import path
from .views import (
    CategoryView,
    StackListView,
)


urlpatterns = [
    path("category/", CategoryView.as_view(), name="category"),
    path("stack-list/", StackListView.as_view(), name="stack-list"),
]
