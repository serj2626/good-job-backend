from django.urls import path
from .views import (
    ChatListView,
    MessageDetailView,
    MessageListView,
    InterviewListView,
    InterviewDetailView,
)


urlpatterns = [
    path("", ChatListView.as_view(), name="chats"),
    path("<int:chat_id>/", MessageListView.as_view(), name="messages"),
    path(
        "<int:chat_id>/<int:msg_pk>/", MessageDetailView.as_view(), name="message"
    ),
    path("interviews/", InterviewListView.as_view(), name="interviews"),
    path(
        "interviews/<int:interview_id>/",
        InterviewDetailView.as_view(),
        name="interview",
    ),
]
