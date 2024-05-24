# serializers.py
from rest_framework import serializers
from .models import Emergency

class EmergencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Emergency
        fields = ['id', 'user', 'message', 'location', 'timestamp']
        read_only_fields = ['user']
