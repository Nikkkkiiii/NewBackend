from django.contrib import admin
from django.urls import path
from .views import LoginView, OTPView, RegisterView, SaveProfileView, TokenView, updateProfileView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('signup/', RegisterView.as_view()),
    path('otpVerification/', OTPView.as_view()),
    path('token/', TokenView.as_view()),
    path('update_profile/', updateProfileView.as_view()),
    path('saveProfile/', SaveProfileView.as_view()),


]
