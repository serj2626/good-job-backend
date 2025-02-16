from .models import Notification
from rest_framework.response import Response
from .serializers import NotificationSerializer
from rest_framework import generics
from drf_spectacular.utils import extend_schema


class NotificationView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    @extend_schema(
        tags=["Уведомления компании"],
        summary="Добавление уведомления компании",
        request=NotificationSerializer,
    )
    def post(self, request, *args, **kwargs):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @extend_schema(
        tags=["Уведомления компании"],
        summary="Получение всех уведомлений компании",
        request=NotificationSerializer,
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    @extend_schema(
        tags=["Уведомления"],
        summary="Получение уведомления по id",
        request=NotificationSerializer,
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Уведомления"],
        summary="Обновление уведомления по id",
        request=NotificationSerializer,
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=["Уведомления"],
        summary="Частичное обновление уведомления по id",
        request=NotificationSerializer,
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        tags=["Уведомления"],
        summary="Удаление уведомления по id",
        request=NotificationSerializer,
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
