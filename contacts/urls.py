from django.urls import path
from .views import FeedbackView, SubscriptionView


urlpatterns = [
    path("feedback/", FeedbackView.as_view(), name="feedback"),
    path("subscription/", SubscriptionView.as_view(), name="subscription"),
]
