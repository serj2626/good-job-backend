from django.shortcuts import render
from .models import NotificationCompany, NotificationEmployee
from rest_framework.response import Response
from .serializers import NotificationCompanySerializer, NotificationEmployeeSerializer
from rest_framework import generics
from drf_spectacular.utils import extend_schema


class NotificationCompanyView(generics.ListAPIView):
    queryset = NotificationCompany.objects.all()
    serializer_class = NotificationCompanySerializer

    @extend_schema(
        tags=["Уведомления компании"],
        summary="Добавление уведомления компании",
        request=NotificationCompanySerializer,
    )
    def post(self, request, *args, **kwargs):
        serializer = NotificationCompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @extend_schema(
        tags=["Уведомления компании"],
        summary="Получение всех уведомлений компании",
        request=NotificationCompanySerializer,
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class NotificationCompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NotificationCompany.objects.all()
    serializer_class = NotificationCompanySerializer

    @extend_schema(
        tags=["Уведомления компании"],
        summary="Получение уведомления компании по id",
        request=NotificationCompanySerializer,
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Уведомления компании"],
        summary="Обновление уведомления компании по id",
        request=NotificationCompanySerializer,
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=["Уведомления компании"],
        summary="Частичное обновление уведомления компании по id",
        request=NotificationCompanySerializer,
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        tags=["Уведомления компании"],
        summary="Удаление уведомления компании по id",
        request=NotificationCompanySerializer,
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class NotificationEmployeeView(generics.ListAPIView):
    queryset = NotificationEmployee.objects.all()
    serializer_class = NotificationEmployeeSerializer

    @extend_schema(
        tags=["Уведомления сотрудника"],
        summary="Добавление уведомления сотруднику",
        request=NotificationEmployeeSerializer,
    )
    def post(self, request, *args, **kwargs):
        serializer = NotificationEmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @extend_schema(
        tags=["Уведомления сотрудника"],
        summary="Получение всех уведомлений сотрудника",
        request=NotificationEmployeeSerializer,
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class NotificationEmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NotificationEmployee.objects.all()
    serializer_class = NotificationEmployeeSerializer

    @extend_schema(
        tags=["Уведомления сотрудника"],
        summary="Получение уведомления сотрудника по id",
        request=NotificationEmployeeSerializer,
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Уведомления сотрудника"],
        summary="Обновление уведомления сотрудника по id",
        request=NotificationEmployeeSerializer,
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=["Уведомления сотрудника"],
        summary="Частичное обновление уведомления сотрудника по id",
        request=NotificationEmployeeSerializer,
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        tags=["Уведомления сотрудника"],
        summary="Удаление уведомления сотрудника по id",
        request=NotificationEmployeeSerializer,
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
