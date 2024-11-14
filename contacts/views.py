from .serializers import FeedbackSerializer, SubscriptionSerializer
from .models import Feedback, Subscription
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import CreateAPIView


class FeedbackView(CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    @extend_schema(summary="Отправка обратной связи")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class SubscriptionView(CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    @extend_schema(summary="Подписка на новости")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
