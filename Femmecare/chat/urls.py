from django.urls import path
from .views import ChatbotListView

urlpatterns = [
    path('chatbotlist/', ChatbotListView.as_view()),
]