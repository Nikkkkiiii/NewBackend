from django.http import JsonResponse
from rest_framework.views import APIView
from map.models import MapMarker

# Create your views here.
class MapView(APIView):
    def get(request):
        hospitals = MapMarker.objects.all()
        data = [{'name': hospital.name, 'lat': hospital.latitude, 'lng': hospital.longitude} for hospital in hospitals]
        return JsonResponse({'hospitals': data})
        
