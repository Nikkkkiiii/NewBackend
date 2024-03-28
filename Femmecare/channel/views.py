from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from User.models import User
from channel.models import Article
from channel.serializer import ArticleSerializer

class ArticleView(APIView):
    def get(self, request):
        User = request.User
        if User.is_authenticated:
            article = article.objects.filter(is_verified = True)
            article_data = []

            for each_article in article:
                User = User.objects.get(email = each_article.author )
                article_data.append({"article_id": each_article.id,
                                    "article_title": each_article.article_title,
                                    "article_content": each_article.article_content,
                                    "article_image": f"media/{each_article.article_image}",
                                    "article_date": each_article.post_date,
                                    "user_name": f"{User.first_name} {User.last_name}",
                                    "user_id": User.id
                                    })
                
            serialized_article_data = ArticleSerializer(each_article, many= True).data
                
            return Response(serialized_article_data)    


    def post(self, request):
        try:
            user_id = request.data['author']
            article_title = request.data['article_title']
            article_content = request.data['article_content']
            article_image = request.FILES['article_image']

            author = User.objects.get(id=user_id)


        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=400)
        except KeyError as e:
            return Response({"error": f"Missing required field: {str(e)}"}, status=400)

        article = Article.objects.create(
            author=author,
            article_image=article_image,
            article_title=article_title,
            article_content=article_content,
        )
        
        return Response({"success": "Successfully posted news"})
