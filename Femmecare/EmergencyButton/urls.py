
from django.urls import path, include  # new
from EmergencyButton.views import *
urlpatterns = [
    path('click', EmergencyButtonView.as_view(), name='emergency_button'),
]
