from django.urls import path
from django.contrib import admin
from .views import ArticleView

urlpatterns = [
    path('article/', ArticleView.as_view())
]