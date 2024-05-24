from rest_framework import serializers
from User.models import User
from .models import Article

class ArticleSerializer(serializers.Serializer):
    article_id = serializers.IntegerField()
    article_title = serializers.CharField()
    article_content = serializers.CharField()
    Image = serializers.CharField()
    article_date = serializers.DateTimeField()
    user_name = serializers.CharField()
    user_id = serializers.CharField()