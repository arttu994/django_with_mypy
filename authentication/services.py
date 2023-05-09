from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from django.core.mail import EmailMultiAlternatives
from rest_framework.exceptions import ValidationError

from authentication.models import User


class UserService:
    def __init__(self):
        self.__user = get_user_model()

    def assign_role(self, token, user):
        user = self.__user.objects.get(username=user)
        if user.is_staff or user.is_superuser:
            token["role"] = "admin"
        else:
            token["role"] = "user"

        return token

    def create_user(self, validated_data, is_active):
        password = validated_data.pop("password", None)
        validate_password(password)
        users_group = Group.objects.get_or_create(name="users_groups")
        user = self.__user.objects.create(**validated_data, is_active=is_active)
        user.set_password(password)
        user.groups.add(users_group[0].id)
        user.save()
        return user

    def get_user_by_activation_code(self, activation_code):
        return self.__user.objects.filter(activation_code=activation_code)

    def activate_user(self, user: User):
        user.is_active = True
        user.save()


def send_mail(email, uuid):
    msg = EmailMultiAlternatives(
        subject="Registration",
        from_email="qwe@gmail.com",
        to=[
            email,
        ],
    )
    html = f"To continue registration click a link <a href=http://localhost:8000/auth/activate/{uuid}>http://localhost:8000/auth/activate/{uuid}</a>"
    msg.attach_alternative(html, "text/html")
    msg.send()
