from django.urls import path
from map.views import MapView

urlpatterns = [
    path('hospital/', MapView.as_view()),
]
