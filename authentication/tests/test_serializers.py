import pytest
from rest_framework_simplejwt.authentication import JWTAuthentication

from authentication.serializers import CustomTokenObtainViewSerializer, SignupSerializer


def test_serializers_creates():
    custom_token = CustomTokenObtainViewSerializer()
    signup = SignupSerializer()

    assert custom_token is not None
    assert signup is not None


@pytest.mark.django_db
def test_get_token(active_user):
    token = CustomTokenObtainViewSerializer.get_token(active_user)
    jwt_auth = JWTAuthentication()

    user = jwt_auth.get_user(token)

    assert user.username == active_user.username
    assert user.email == active_user.email
    assert user.is_active == active_user.is_active


@pytest.mark.django_db
@pytest.mark.parametrize(
    "validated_data",
    [
        ({"username": "qaz", "email": "qaz@gmail.com", "password": "Hellomotto1"}),
        ({"username": "wsx", "email": "wsx@gmail.com", "password": "Hellomotto1"}),
    ],
)
def test_create(validated_data):
    usr = SignupSerializer().create(validated_data)

    assert usr is not None
    assert usr.username == validated_data["username"]
    assert usr.email == validated_data["email"]
    assert usr.is_active == False
