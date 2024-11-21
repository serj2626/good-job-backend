from .models import Category, Stack
from .serializers import CategorySerializer, StackSerializer
from drf_spectacular.utils import extend_schema
from rest_framework import generics


class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    @extend_schema(
        tags=["Категории"],
        responses=CategorySerializer,
        summary="Получение категории",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class StackListView(generics.ListAPIView):
    serializer_class = StackSerializer
    queryset = Stack.objects.all()

    @extend_schema(
        tags=["Стеки"],
        responses=StackSerializer,
        summary="Получение всех стеков",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
