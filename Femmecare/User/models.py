
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
# from django.urls import reverse

# Create your models here.
class User(AbstractUser, PermissionsMixin):
    # common attributes
    phone_number = models.CharField(max_length= 12, unique=True)
    address = models.CharField(max_length=255)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    username = models.CharField( null=True,blank=True,max_length=50, unique=True)
    profileImage = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return f"{self.email}"


    # User types
    USER_TYPES = (
        ('femme', 'Normal user'),
        ('doctor', 'Health personnel')
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='normal')
    
    REQUIRED_FIELDS=['phone_number', 'firstName', 'lastName', 'password', 'email', 'address']
