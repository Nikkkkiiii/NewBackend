from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'phone_number', 'password','address')


        # 'username': email, 
        #   'password': password,
        #   'phonenumber': phone_number, 
        #   'address': address
