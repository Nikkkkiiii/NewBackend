from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from User.models import User
from channel.models import Article
from channel.serializer import ArticleSerializer
from rest_framework import status


class ArticleView(APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            article = Article.objects.filter()
            article_data = []

            for each_article in article:
                user = User.objects.get(email = each_article.author )
                article_data.append({"article_id": each_article.id,
                                    "article_title": each_article.article_title,
                                    "article_content": each_article.article_content,
                                    "Image": f"media/{each_article.Image}",
                                    "article_date": each_article.post_date,
                                    "user_name": user.username,
                                    "user_id": user.id
                                    })
                
            serialized_article_data = ArticleSerializer(article_data, many= True).data
                
            return Response(serialized_article_data)    

class PostArticleView(APIView):
    def post(self, request):
        user = request.user
        print(request.user)
        print(request.data)
        if user.is_authenticated:
            try:
                article_title = request.data['article_heading']
                article_content = request.data['article_description']
                # Image = request.FILES['Image']
                author = user.id
            except User.DoesNotExist:
                print("me here")
                return Response({"error": "User does not exist"}, status=400)
            except KeyError as e:
                print("me heghre")
                return Response({"error": f"Missing required field: {str(e)}"}, status=400)
    
            article = Article.objects.create(
                author=user,
                # Image=Image,
                article_title=article_title,
                article_content=article_content,
            )
            
            return Response({"success": "Successfully posted article."})
    

    def put(self, request):
        user = request.user
        if user.is_authenticated:
            try:
                article_id =request.data["article_id"]
                article = Article.objects.get(id=article_id)
                article_title = request.data.get('article_heading')
                article.Image = request.data.get('Image')
                article_Content = request.data.get('article_description')
                article.article_title = article_title
                article.article_content = article_Content
                article.save()
            except Article.DoesNotExist:
                return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)
    
        return Response({"Success": "Successfully updated"}, status=200)

    def delete(self, request):
        user = request.user
        if user.is_authenticated:
            try:
                article_id = request.data["article_id"]
                article = Article.objects.get(id=article_id)
                article.delete()
                return Response({"success": "Article deleted successfully"}, status=200)
            except Article.DoesNotExist:
                return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)


            
