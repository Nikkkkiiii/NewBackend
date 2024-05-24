from django.contrib import admin
from channel.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','article_title','article_content','author','post_date')
    search_fields = ('article_title','article_content','author')

admin.site.register(Article, ArticleAdmin)
