import pytest

from django.urls import reverse

from authentication.views import ActivationView, CustomTokenObtainPairView, SignupView


def test_views_works():
    active = ActivationView()
    custom = CustomTokenObtainPairView()
    signup = SignupView()

    assert active is not None
    assert custom is not None
    assert signup is not None


@pytest.mark.django_db
def test_activation_view_get(api_client, get_activation_code):
    activation_code, response = get_activation_code
    status_code, data = response
    print(f"activation_code {activation_code}, response {response}")
    url = reverse(
        "activate",
        args=(activation_code,),
    )
    response = api_client.get(url)

    assert response.status_code == status_code
    assert response.data.startswith(data)


@pytest.mark.django_db
def test_signup_view_post_response(api_client):
    url = reverse("signup")
    response = api_client.post(
        url,
        {"username": "qwe", "email": "qwe@gmail.com", "password": "Hellomotto1"},
    )

    assert response.status_code == 201
