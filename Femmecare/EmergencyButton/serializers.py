from rest_framework import serializers
from .models import EmergencyButton

class EmergencyButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyButton
        fields = ['location', 'message', 'sent_to']
