import pytest

from authentication.helpers import user_success_msg


def test_user_success_msg():
    username = "qwe"
    email = "qwe@gmail.com"
    msg = f"User {username} has been created. To activate confirm the link sent into {email}"
    result = user_success_msg(username, email)

    assert result == msg
