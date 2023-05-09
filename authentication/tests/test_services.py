import pytest

from authentication.services import UserService


@pytest.mark.django_db
def test_user_service_has_attrs(user_service):
    assert hasattr(user_service, "_UserService__user")


@pytest.mark.django_db
def test_assign_role(user, user_service):
    user_name = user[0].username
    expected = user[1]
    role_assigned = user_service.assign_role({}, user_name)
    result = role_assigned["role"] == "admin"

    assert result == expected


@pytest.mark.django_db
@pytest.mark.parametrize(
    "validated_data,is_active",
    [
        (
            {"username": "qaz", "email": "qaz@gmail.com", "password": "Hellomotto1"},
            True,
        ),
        (
            {"username": "wsx", "email": "wsx@gmail.com", "password": "Hellomotto1"},
            False,
        ),
    ],
)
def test_create_user(validated_data, is_active, user_service):
    pwd = validated_data.get("password")
    user = user_service.create_user(validated_data, is_active)
    assert user.username == validated_data["username"]
    assert user.email == validated_data["email"]
    assert user.is_active == is_active
    assert user.check_password(pwd)


@pytest.mark.django_db
def test_get_user_by_activation_code(user, user_service):
    usr = user[0]
    result = user_service.get_user_by_activation_code(usr.activation_code).get()

    assert result.username == usr.username
    assert result.email == usr.email
    assert result.activation_code == usr.activation_code


@pytest.mark.django_db
def test_activate_user(non_active_user, user_service):
    user_service.activate_user(non_active_user)
    assert non_active_user.is_active == True
