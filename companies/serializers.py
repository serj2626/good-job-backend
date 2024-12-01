from rest_framework import serializers
from accounts.serializers import UserDataSerializer
from companies.models import Company, Vacancy, Comment
from django.utils.timesince import timesince


class CompanySerializer(serializers.ModelSerializer):
    user = UserDataSerializer()
    stacks = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    count_vacancies = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()

    def get_count_vacancies(self, obj):
        return obj.vacancies.count()

    def get_full_name(self, obj):
        return f'{obj.get_type_display()} {obj.name}'

    class Meta:
        model = Company
        fields = "__all__"


class VacancySerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    stacks = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    category = serializers.CharField(source="category.get_name_display")
    work_schedule = serializers.CharField(source="get_work_schedule_display")
    level = serializers.CharField(source="get_level_display")
    time_ago = serializers.SerializerMethodField()

    def get_time_ago(self, obj):
        return timesince(obj.created_at)

    class Meta:
        model = Vacancy
        fields = "__all__"


class VacancyListCreateSerializer(serializers.ModelSerializer):
    # company = serializers.HiddenField(default=serializers.CurrentUserDefault())
    company = CompanySerializer()
    stacks = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    category = serializers.CharField(source="category.get_name_display")
    work_schedule = serializers.CharField(source="get_work_schedule_display")
    level = serializers.CharField(source="get_level_display")
    time_ago = serializers.SerializerMethodField()

    def get_time_ago(self, obj):
        return timesince(obj.created_at)

    class Meta:
        model = Vacancy
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CompanyDetailSerializer(serializers.ModelSerializer):
    user = UserDataSerializer()
    vacancies = VacancySerializer(many=True)
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return f'{obj.get_type_display()} {obj.name}'

    class Meta:
        model = Company
        fields = "__all__"
