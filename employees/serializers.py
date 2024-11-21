from rest_framework import serializers
from accounts.serializers import UserDataSerializer
from employees.models import Employee, Experience, Resume


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserDataSerializer()

    class Meta:
        model = Employee
        fields = "__all__"


class ResumeListCreateSerializer(serializers.ModelSerializer):
    employee = serializers.HiddenField(default=serializers.CurrentUserDefault())
    stacks = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    category = serializers.CharField(source="category.name")

    class Meta:
        model = Resume
        fields = "__all__"


class ResumeSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    # employee = serializers.HiddenField(default=serializers.CurrentUserDefault())
    stacks = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    category = serializers.CharField(source="category.name")

    class Meta:
        model = Resume
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"
