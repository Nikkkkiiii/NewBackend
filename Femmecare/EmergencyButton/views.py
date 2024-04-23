from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EmergencyButton

class EmergencyButtonView(APIView):
    def post(self, request):
        message = request.data.get('message')
        if not message:
            return Response({'error': 'Message field is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Save the emergency message to the database
        EmergencyButton.objects.create(message=message)
        
        return Response({'message': 'Emergency message saved successfully.'}, status=status.HTTP_201_CREATED)
    
    
