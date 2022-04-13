from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('activate/', ActivationView.as_view(), name='activation'),
    path('login/', LoginView.as_view(), name='signin'),
    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('change_password/', ChangePasswordView.as_view(), name='change-password'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]