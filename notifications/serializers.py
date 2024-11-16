from rest_framework import serializers
from .models import NotificationCompany, NotificationEmployee


class NotificationCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationCompany
        fields = "__all__"


class NotificationEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationEmployee
        fields = "__all__"
