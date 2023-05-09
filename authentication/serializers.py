from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authentication.models import User
from authentication.services import UserService


class CustomTokenObtainViewSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        user_service = UserService()
        token = super().get_token(user)
        token = user_service.assign_role(token, user)
        return token


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "password", "email", "activation_code"]
        extra_kwargs = {
            "password": {"write_only": True},
            "id": {"read_only": True},
            "activation_code": {"read_only": True},
        }

    def create(self, validated_data):
        user_service = UserService()
        return user_service.create_user(validated_data, is_active=False)
