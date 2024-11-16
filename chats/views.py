from .serializers import (
    ResponseVacancySerializer,
    MessageSerializer,
    InterviewSerializer,
)
from .models import ResponseVacancy, Message

# from rest_framework import viewsets, permissions
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import action
# from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from drf_spectacular.utils import extend_schema


class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    @extend_schema(
        tags=["Отклики и сообщения"],
        responses=MessageSerializer,
        summary="Получение сообщения по id",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Отклики и сообщения"],
        request=MessageSerializer,
        responses=MessageSerializer,
        summary="Обновление сообщения по id",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=["Отклики и сообщения"],
        request=MessageSerializer,
        responses=MessageSerializer,
        summary="Удаление сообщения по id",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(
        tags=["Отклики и сообщения"],
        request=MessageSerializer,
        responses=MessageSerializer,
        summary="Частичное обновление сообщения по id",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


class MessageListView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        return super().get_queryset().filter(chat=self.kwargs["chat_id"])

    @extend_schema(
        tags=["Отклики и сообщения"],
        request=MessageSerializer,
        responses=MessageSerializer,
        summary="Добавление сообщения",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        tags=["Отклики и сообщения"],
        responses=MessageSerializer,
        summary="Получение всех сообщений",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ChatListView(generics.ListCreateAPIView):
    queryset = ResponseVacancy.objects.all()
    serializer_class = ResponseVacancySerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    @extend_schema(
        tags=["Отклики и сообщения"],
        request=ResponseVacancySerializer,
        responses=ResponseVacancySerializer,
        summary="Добавление чата",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        tags=["Отклики и сообщения"],
        responses=ResponseVacancySerializer,
        summary="Получение всех чатов",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class InterviewListView(generics.ListCreateAPIView):
    queryset = InterviewSerializer
    serializer_class = InterviewSerializer

    @extend_schema(
        tags=["Интервью"],
        responses=InterviewSerializer,
        summary="Получение всех интервью",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Интервью"],
        request=InterviewSerializer,
        responses=InterviewSerializer,
        summary="Добавление интервью",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class InterviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InterviewSerializer
    serializer_class = InterviewSerializer

    @extend_schema(
        tags=["Интервью"],
        responses=InterviewSerializer,
        summary="Получение интервью по id",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Интервью"],
        request=InterviewSerializer,
        responses=InterviewSerializer,
        summary="Обновление интервью по id",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=["Интервью"],
        request=InterviewSerializer,
        responses=InterviewSerializer,
        summary="Удаление интервью по id",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(
        tags=["Интервью"],
        request=InterviewSerializer,
        responses=InterviewSerializer,
        summary="Частичное обновление интервью по id",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


# class MessagePagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = "page_size"
#     max_page_size = 1000


# class MessageViewSet(viewsets.ModelViewSet):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#     pagination_class = MessagePagination

#     def get_permissions(self):
#         if self.action == "create":
#             permission_classes = [permissions.IsAuthenticated]
#         else:
#             permission_classes = [permissions.AllowAny]
#         return [permission() for permission in permission_classes]
