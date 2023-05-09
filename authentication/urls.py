from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from authentication.views import CustomTokenObtainPairView, SignupView, ActivationView

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("signin/", CustomTokenObtainPairView.as_view(), name="signin"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("activate/<uuid:activation_code>", ActivationView.as_view(), name="activate"),
]
