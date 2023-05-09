from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from authentication.serializers import CustomTokenObtainViewSerializer, SignupSerializer
from authentication.services import UserService
from authentication.tasks import send_email
from authentication.helpers import user_success_msg


class SignupView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

    def post(self, request: Request):
        serializer = self.get_serializer(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        except ValidationError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=e)

        username = serializer.data.get("username")
        email = serializer.data.get("email")
        uuid = serializer.data.get("activation_code")
        send_email.delay(email, uuid)

        return Response(
            {"success": user_success_msg(username, email)},
            status=status.HTTP_201_CREATED,
        )


class ActivationView(APIView):
    permission_classes = [
        AllowAny,
    ]

    def get(self, request: Request, activation_code):
        user_service = UserService()
        current_user = user_service.get_user_by_activation_code(activation_code)
        if not current_user.exists():
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data=f"User with code {activation_code} not found",
            )
        user_service.activate_user(current_user.get())
        return Response(status=status.HTTP_200_OK, data="User is activated")


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainViewSerializer
    permission_classes = [
        AllowAny,
    ]
