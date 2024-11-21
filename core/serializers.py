from .models import (
    Category,
    Stack,
)
from rest_framework import serializers


class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
