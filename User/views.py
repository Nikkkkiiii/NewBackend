from django.shortcuts import render
import pyotp
from rest_framework.views import APIView
from User.models import MobileTokens, User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import update_last_login
from rest_framework.response import Response
from .serializer import RegisterSerializer, UserSerializer
from .utils import send_otp, sendEmail
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password

# Create your views here.

def user_image_path(instance, filename):
    phone_no = instance.phone_number
    filename = str(filename).split('.')[-1]
    return f'user_images/{phone_no}.{filename}'

class LoginView(APIView):

    def post(self, request):
        data = request.data

        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            return Response({'status': 404, 'message': 'No such user found'}, status=404)
        
        if not check_password(data['password'], user.password):
            return Response({'status': 401, 'message': 'Wrong password'}, status=401)

        user = authenticate(request, username=user.username, password=data['password'])
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            serializer = UserSerializer(user)
            return Response({
                'status': 200,
                'user': serializer.data,
                'refresh': str(refresh),
                'access_token': str(refresh.access_token),
                'message': 'Login successful'
            }, status=200)
        else:
            return Response({'status': 401, 'message': 'Authentication failed'}, status=401)
        
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    class LogoutView(APIView):
        def post(self, request):
            phone_key = request.data['phone_key']
            mobile_token = MobileTokens.objects.get(phone_key = phone_key)
            mobile_token.is_logged_in = False
            mobile_token.save()

            return Response({'success': 'Success'}, status=status.HTTP_200_OK)

class RegisterView(APIView):

    def post(self, request):
        print(request.data)

        serializer = RegisterSerializer(data=request.data)

        # username = request.data['username']
        # email = request.data['email']
        # phone_number = request.data['phone_number']
        # password = request.data['password']
        # address = request.data['address']

        # print(username, email, phone_number, password, address)



        # serializer = RegisterSerializer(data=request.data)
        # user = User.objects.create(username=username, email= email, phone_number=phone_number,address=address,is_active=False)

        # user.set_password(password)
        # user.save()

        if serializer.is_valid():
            user = serializer.save()
            user.is_active = False
            # Hash the password
            user.set_password(serializer.validated_data['password'])
            user.save()

            otp, otp_key = send_otp(request)
            message = f" Your otp for registration continuation is {otp}."
            subject = "OTP code verification"
            email = serializer.validated_data['email']
            sendEmail(request, [email], message, subject)
            print (otp)

            return Response({ 'otp_key': otp_key, 'email': email })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
        #     # return Response({'success': 'Enter verification code for successful registeration.', 'otp_key': otp_key, 'email': email })
        # return Response({'success': 'Enter verification code for successful registeration.'})
        
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        # Retrieve all users
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
        
class OTPView(APIView):
    def post(self, request):
        otp = request.data['entered_otp']

        print(otp)
        send_Email =  request.data['email']
        otp_key = request.session['otp_key']
        purpose = request.data['purpose']
        # otp_valid_until = request.session['otp_valid_date']


        if otp_key is not None:
            totp = pyotp.TOTP(otp_key, interval= 600)
            if totp.verify(otp):
                # print("inside verification")
                user = User.objects.get(email= send_Email)
                if purpose== "signup":
                    user.is_active = True
                    user.save()
                elif purpose == "reset":
                    newpass = request.data['new_password']
                    user.set_password(newpass)
                    user.save()
            
                return Response({"success": "successful registration"})
            else:
                return Response({"error": "Wrong OTP or time out."})

                
        return Response({"error": "Sorry, something went wrong."})

class ResetPassword(APIView):
    def post(self, request):
        try:
            email = request.data['email']
            otp, otp_key = send_otp(request)
            message = f" Your otp for password reset continuation is {otp}."
            subject = "Password reset"
            sendEmail(request, [email], message, subject)
            return Response({'otp_key': otp_key, 'email': email })
        except:
            return Response(KeyError)

class TokenView(APIView):
    permission_classes=[IsAuthenticated]
    
    # @login_required
    def get(self, request):
        return Response({'hii': 'good job'})
    

class SaveProfileView(APIView):
    def Post(self, request):
        user = request.user
        user_id = request.data.get('user')
        viewProfileDetails = []

        if user.is_authenticated:
            try:
                user_details = User.objects.get(id=user_id)

                profile_data = {
                    "user_id": user_details.id,
                    "user_fullname": f"{user_details.first_name} {user_details.last_name}",
                    "user_name": user_details.username,
                    "user_location": user_details.address,
                    "user_contact": user_details.phone_number,
                    "user_email": user_details.email,
                    # Assuming image is a FileField or ImageField
                    "user_image": user_details.profileImage.url if user_details.profileImage else None,  
                    "user_type": user_details.user_type,
                }
                viewProfileDetails.append(profile_data)

            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=404)
            
            serialized_view_profile_data = UserSerializer(viewProfileDetails, many=True).data

            return Response(serialized_view_profile_data)
        else:
            return Response({'error': 'user not authenticated'}, status=401)
                

    
class updateProfileView(APIView):

    def post(self, request):
        user = request.user
        name = request.data['name']
        email = request.data['email']
        # print(request)

        # print(user)
        print(request.POST)

        # if user.is_authenticated:
        #     try:
        #         if user.user_type == "business":
        #             business = Business.objects.get(user=user)
        #             for key, value in request.POST.items():
        #                 if key in ['name', 'description']:
        #                     setattr(business, key, value)
        #             business.save()
                
        #         if 'image' in request.FILES:
        #                 print("Image")
        #                 user.image=request.FILES['image']
                        
        #         for key, value in request.POST.items():
        #             print(key,value)
        #             if hasattr(user, key):
        #                 setattr(user, key, value)
        #         user.save()
        #         return Response({'data': "success"})
        #     except Business.DoesNotExist:
        #         return Response({"error": "Does not found any business"})
        # else:
        #     return Response({"error": "User is not authenticated"}) 

        if user.is_authenticated:
            try:
                if 'profileImage' in request.FILES:
                    print("profileImage")
                    user.profileImage=request.FILES['profileImage']

                user.name = name
                user.email = email
                user.save()
                return Response({'data': "success"})
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=404)

        

            # return Response({"success": "Successfully updated"}, status= status.HTTP_200_OK)
        else:
            return Response({'error': 'User not authenticated'}, status=401)
