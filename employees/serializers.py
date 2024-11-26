from datetime import datetime
import django
from rest_framework import serializers
from accounts.serializers import UserDataSerializer
from core.serializers import CategorySerializer
from employees.models import Employee, Experience, Resume, Project, Education
from django.utils.timesince import timesince


class EducationSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="get_type_display")

    class Meta:
        model = Education
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    stacks = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    category = serializers.CharField(source="category.name")
    time_ago = serializers.SerializerMethodField()

    def get_time_ago(self, obj):
        return timesince(obj.created_at)

    class Meta:
        model = Project
        fields = "__all__"


class ResumeListCreateSerializer(serializers.ModelSerializer):
    employee = serializers.HiddenField(default=serializers.CurrentUserDefault())
    stacks = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    category = serializers.CharField(source="category.name")

    class Meta:
        model = Resume
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    stacks = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    category = CategorySerializer()

    class Meta:
        model = Experience
        fields = "__all__"


class ResumeSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(source="employee.projects", many=True)
    stacks = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    category = serializers.CharField(source="category.name")
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return obj.employee.first_name + " " + obj.employee.last_name

    class Meta:
        model = Resume
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    resumes = ResumeSerializer(many=True)
    user = UserDataSerializer()
    stacks = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    projects = ProjectSerializer(many=True)
    age = serializers.SerializerMethodField()
    gender = serializers.CharField(source="get_gender_display")
    experiences = ExperienceSerializer(many=True)
    educations = EducationSerializer(many=True)

    def get_age(self, obj):
        return datetime.now().year - obj.date_of_birth.year

    class Meta:
        model = Employee
        fields = "__all__"
