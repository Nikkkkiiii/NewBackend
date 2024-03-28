from django.db import models

class EmergencyButton(models.Model):
    location = models.CharField(max_length=255, null=False)
    message = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    sent_to = models.CharField(max_length=255)


