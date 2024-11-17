from rest_framework import serializers

from common.const import USER_TYPES
from .models import Profile, User
from enum import Enum


class UserType(Enum):
    Company = "Компания"
    Employee = "Работник"


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "name", "type"]


class ProfileSerializer(serializers.ModelSerializer):
    user = UserDataSerializer()
    class Meta:
        model = Profile
        fields = "__all__"


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    type = serializers.ChoiceField(
        choices=USER_TYPES, default=UserType.Employee.value
    )

    # type = serializers.CharField(source="get_type_display")

    class Meta:
        model = User
        fields = ["email", "name", "type", "password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        email = self.validated_data["email"]
        name = self.validated_data["name"]
        type = self.validated_data["type"]

        if password != password2:
            raise serializers.ValidationError("Пароли не совпадают!")

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                "Пользователь с такой почтой уже существует!"
            )
        new_user = User(email=email, name=name, type=type)
        new_user.set_password(password)
        new_user.save()
        return new_user
