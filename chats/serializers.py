from rest_framework import serializers
from .models import ResponseVacancy, MessageToResponse, Interview


class MessageToResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageToResponse
        fields = "__all__"


class ResponseVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseVacancy
        fields = "__all__"


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = "__all__"
