from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.decorators import (
    api_view,
)
from rest_framework.response import Response

from .models import User
from .serializers import UserRegisterSerializer


@extend_schema(summary="Получение информации о пользователе")
@api_view(["GET"])
def get_user_info(request):
    user = request.user
    return Response({"email": user.email, "type": user.type})


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

    @extend_schema(summary="Регистрация пользователя")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    lookup_field = "slug"
