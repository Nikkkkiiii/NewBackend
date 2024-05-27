from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EmergencyButton
from .serializers import EmergencyButtonSerializer

class EmergencyButtonView(APIView):
    def post(self, request):
        # Deserialize and validate the incoming data
        serializer = EmergencyButtonSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Save the validated data to the database
                serializer.save()
            except Exception as e:
                # Return a generic error response if something goes wrong
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            # Return a success response
            return Response({'message': 'Emergency message saved successfully.'}, status=status.HTTP_201_CREATED)
        
        # Return a response with validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
