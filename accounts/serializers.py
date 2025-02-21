from rest_framework import serializers

from common.const import USER_TYPES
from .models import User


class UserDataSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="get_type_display")

    class Meta:
        model = User
        fields = [
            "email",
            "type",
            "online"
        ]


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    type = serializers.ChoiceField(choices=USER_TYPES, default="Employee")

    # type = serializers.CharField(source="get_type_display")

    class Meta:
        model = User
        fields = ["email", "type", "password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        email = self.validated_data["email"]
        type = self.validated_data["type"]

        if password != password2:
            raise serializers.ValidationError("Пароли не совпадают!")

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                "Пользователь с такой почтой уже существует!"
            )
        new_user = User(email=email, type=type)
        new_user.set_password(password)
        new_user.save()
        return new_user
