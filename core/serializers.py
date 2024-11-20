from .models import (
    Category,
    Resume,
    Vacancy,
    Comment,
    Experience,
    Stack,
    Employee,
    Company,
    FavoriteResume,
    FavoriteVacancy,
)
from rest_framework import serializers
from accounts.serializers import UserDataSerializer


class CompanySerializer(serializers.ModelSerializer):
    user = UserDataSerializer()

    class Meta:
        model = Company
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserDataSerializer()

    class Meta:
        model = Employee
        fields = "__all__"


class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ResumeSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    stacks = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    category = serializers.CharField(source="category.name")

    class Meta:
        model = Resume
        fields = "__all__"


class VacancySerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    stacks = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    category = serializers.CharField(source="category.name")

    class Meta:
        model = Vacancy
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"


class FavoriteResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteResume
        fields = "__all__"


class FavoriteVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteVacancy
        fields = "__all__"
