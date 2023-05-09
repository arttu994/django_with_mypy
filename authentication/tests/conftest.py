import pytest

from uuid import uuid4

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.models import User
from authentication.services import UserService


@pytest.fixture
def user_service():
    return UserService()


@pytest.fixture(
    params=[
        (("qwe", "qwe@gmail.com", True, True, "rty"), True),
        (("asd", "asd@gmail.com", True, False, "asd"), False),
    ],
)
def user(db, request):
    user_input, expected = request.param
    user = User()
    user.username = user_input[0]
    user.email = user_input[1]
    user.is_active = user_input[2]
    user.is_staff = user_input[3]
    user.set_password(user_input[4])
    user.save()
    yield user, expected


@pytest.fixture
def non_active_user(db):
    user = User()
    user.username = "ert"
    user.email = "ert@gmail.com"
    user.is_active = False
    user.is_staff = False
    user.set_password("tre")
    user.save()

    return user


@pytest.fixture
def active_user(db):
    user = User()
    user.username = "ert"
    user.email = "ert@gmail.com"
    user.is_active = True
    user.is_staff = False
    user.set_password("tre")
    user.save()

    return user


@pytest.mark.django_db
@pytest.fixture
def api_client():
    client = APIClient()
    user = User.objects.create_superuser(
        "myuser", "myemail@test.com", "Testpassword123"
    )
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Token {refresh.access_token}")

    return client


@pytest.mark.django_db
@pytest.fixture(
    params=[
        ("positive", (200, "User is activated")),
        ("negative", (404, "User with code")),
    ]
)
def get_activation_code(non_active_user, request):
    data, response = request.param
    if data == "positive":
        yield non_active_user.activation_code, response
    if data == "negative":
        yield uuid4(), response
