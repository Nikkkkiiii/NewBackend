from django.contrib import admin
from django.urls import path
from .views import LoginView, RegisterView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('signup/', RegisterView.as_view())
]
