# models.py
from django.db import models
from django.utils import timezone
from User.models import User

class Emergency(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    location = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Emergency from {self.user.username} at {self.timestamp}"
