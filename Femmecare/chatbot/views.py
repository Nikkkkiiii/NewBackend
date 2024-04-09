from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from User.models import User
from chatbot.models import Chatbot
from chatbot.serializers import ChatbotListSerializer, ChatbotSerializer
from django.db.models import Q     

class ChatbotListView(APIView):

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            # user_obj = User.objects.get(email = user)
            messages = Chatbot.objects.filter(
            Q(to=request.user) | Q(user=request.user)
        ).order_by('-created')

        serializer = ChatbotSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        email_user = request.user

        if email_user.is_authenticated:
            print(email_user)
            print("helllllllllllllllllllllloooooooo")
            users = User.objects.exclude(email=email_user.email).filter(
            Q(sent_messages__receiver=request.user) | Q(received_messages__sender=request.user) |
            Q(sent_messages__sender=request.user) | Q(received_messages__receiver=request.user)
            ).distinct()
        
            print("helllllllllllllllllllllloooooooo")

            # Get the latest message for each chat
            message_list = []
            for user in users:
                latest_message = Chatbot.objects.filter(
                    Q(sender=email_user, receiver=user) | Q(sender=user, receiver=email_user)
                ).latest('created')

                # Determine if the message is sent by the logged-in user
                is_sent = latest_message.sender == email_user

                message_list.append({"user_email": user.email,
                                    "user_image": user.profileImage,
                                    "user_fullname": f"{user.first_name} {user.last_name}", 
                                    "my_id": email_user.id,
                                    "user_id": user.id,
                                    "latest_message": latest_message.message, 
                                    "datetime": latest_message.created,
                                    "sent_by_me": is_sent
                                    })
            

            message_list_serializer = ChatbotListSerializer(message_list, many = True).data
            return Response(message_list_serializer)