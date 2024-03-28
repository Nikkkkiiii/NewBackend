from django.contrib import admin
from django.urls import path
from .views import LoginView, OTPView, RegisterView, TokenView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('signup/', RegisterView.as_view()),
    path('otpVerification/', OTPView.as_view()),
    path('token/', TokenView.as_view()),
]
