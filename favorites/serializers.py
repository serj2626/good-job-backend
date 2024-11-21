from rest_framework import serializers

from .models import FavoriteResume, FavoriteVacancy


class FavoriteResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteResume
        fields = "__all__"


class FavoriteVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteVacancy
        fields = "__all__"
