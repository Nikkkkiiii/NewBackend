from django.urls import path
from django.contrib import admin
from .views import ArticleView, PostArticleView

urlpatterns = [
    path('article/', ArticleView.as_view()),
    path('post_article/', PostArticleView.as_view()),
]