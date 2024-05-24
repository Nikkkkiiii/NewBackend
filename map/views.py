# mapapp/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hospital
from .serializers import HospitalSerializer

class HospitalListView(APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            try:
                hospitals = Hospital.objects.all()
                serializer = HospitalSerializer(hospitals, many=True)
                return Response(serializer.data)
            except:
                return Response({"Success": "Successfully retreived"}, status=200)

        return Response({"Success": "Successfully retreived"}, status=200)
       

    def post(self, request):
        user = request.user
        if user.is_authenticated:
            try:
                serializer = HospitalSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({"success": "Successfully posted article."})
        return Response({"success": "Successfully posted article."})
