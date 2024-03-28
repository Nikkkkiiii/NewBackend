from django.db import models
from User.models import User

# Create your models here.
class Chatbot(models.Model):
    sendTo = models.ForeignKey(User, on_delete= models.CASCADE, null = False, related_name='chatbot_messages_received')
    sendFrom = models.ForeignKey(User, on_delete= models.CASCADE, null = False, related_name='chatbot_messages_sent')
    datetime = models.DateTimeField( auto_now_add=True)
    message = models.TextField()