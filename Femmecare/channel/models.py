from django.db import models
from User.models import User
from django.utils.timezone import datetime

class Article(models.Model):
    author = models.ForeignKey(User, related_name = "author", on_delete= models.CASCADE, null = False)
    article_title = models.CharField(max_length= 255)
    article_content = models.TextField()
    Image = models.ImageField(upload_to="media/", blank=True, null=True)
    post_date= models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField(default=datetime.now())


    