from django.db import models
from User.models import User

# Create your models here.
class Messages(models.Model):
    receiver = models.ForeignKey(User, on_delete= models.CASCADE, null = False, related_name='received_messages')
    sender = models.ForeignKey(User, on_delete= models.CASCADE, null = False, related_name='sent_messages')
    created = models.DateTimeField( auto_now_add=True)
    message = models.TextField()
    chat_image = models.ImageField(upload_to="media/", blank=True, null=True)

    class Meta:
        ordering = ['-created'] 


