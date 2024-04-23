from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework import status
from User.models import User
from .models import Messages
from .serializers import ChatbotListSerializer, ChatbotSerializer
from django.db.models import Q 

@method_decorator(csrf_exempt, name='dispatch')
class ChatbotListView(APIView):

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            # user_obj = User.objects.get(email = user)
            messages = Messages.objects.filter(
            Q(to=request.user) | Q(user=request.user)
        ).order_by('-created')

        serializer = ChatbotSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        email_user = request.user

        if email_user.is_authenticated:
            print(email_user)
            users = User.objects.exclude(email=email_user.email).filter(
            Q(sent_messages__receiver=request.user) | Q(received_messages__sender=request.user) |
            Q(sent_messages__sender=request.user) | Q(received_messages__receiver=request.user)
            ).distinct()
        
            print(users)
            # Get the latest message for each chat
            message_list = []
            for user in users:
                print(user)
                print(email_user)
                try:
                    
                    latest_message = Messages.objects.filter(
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
                    
                
                except Exception as e:
                    print(e)
                    return Response(status= 405)

                print(message_list)
            message_list_serializer = ChatbotListSerializer(message_list, many = True).data
            return Response(message_list_serializer)
    