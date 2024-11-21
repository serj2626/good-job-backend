from tokenize import Comment
from rest_framework import serializers
from accounts.serializers import UserDataSerializer
from companies.models import Company, Vacancy


class CompanySerializer(serializers.ModelSerializer):
    user = UserDataSerializer()

    class Meta:
        model = Company
        fields = "__all__"


class VacancySerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    stacks = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    category = serializers.CharField(source="category.name")

    class Meta:
        model = Vacancy
        fields = "__all__"


class VacancyListCreateSerializer(serializers.ModelSerializer):
    company = serializers.HiddenField(default=serializers.CurrentUserDefault())
    stacks = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    category = serializers.CharField(source="category.name")

    class Meta:
        model = Vacancy
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
