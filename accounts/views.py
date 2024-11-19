from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.decorators import (
    api_view,
)
from rest_framework.response import Response

from .models import User
from .serializers import UserRegisterSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

    @extend_schema(summary="Регистрация пользователя")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


    lookup_field = "slug"

    @extend_schema(summary="Получение профиля")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(summary="Обновление профиля")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(summary="Частичное обновление профиля")
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)