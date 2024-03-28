# from datetime import datetime
import random
from django.shortcuts import render
import pyotp
from rest_framework.views import APIView
from User.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import update_last_login
from rest_framework.response import Response
from .serializer import RegisterSerializer
from .utils import send_otp, sendEmail
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate 

# Create your views here.
class LoginView(APIView):

    def post(self, request):
        phone_number = request.data['username']
        password = request.data['password']

        user = authenticate(request, username=phone_number, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(User)

            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            update_last_login(user, user)
            return Response({'token': response_data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        

class RegisterView(APIView):

    def post(self, request):
        print(request.data)
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            user.is_active = False
            # Hash the password
            user.set_password(serializer.validated_data['password'])
            user.save()

            # otp, otp_key = send_otp(request)
            # message = f" Your otp for registration continuation is {otp}."
            # subject = "OTP code verification"
            # email = serializer.validated_data['email']
            # sendEmail(request, [email], message, subject)
            # print (otp)
            
            
            # return Response({'success': 'Enter verification code for successful registeration.', 'otp_key': otp_key, 'email': email })
            return Response({'success': 'Enter verification code for successful registeration.'})
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class OTPView(APIView):
    def post(self, request):
        otp = request.data['entered_otp']

        print(otp)
        send_Email =  request.data['email']
        otp_key = request.session['otp_key']
        # otp_valid_until = request.session['otp_valid_date']


        if otp_key is not None:
            totp = pyotp.TOTP(otp_key, interval= 600)
            if totp.verify(otp):
                # print("inside verification")
                user = User.objects.get(email= send_Email)
                user.is_active = True
                user.save()
                return Response({"success": "successful registration"})
            else:
                return Response({"error": "Wrong OTP or time out."})

                
        return Response({"error": "Sorry, something went wrong."})



class TokenView(APIView):
    permission_classes=[IsAuthenticated]
    
    # @login_required
    def get(self, request):
        return Response({'hii': 'good job'})
    
    