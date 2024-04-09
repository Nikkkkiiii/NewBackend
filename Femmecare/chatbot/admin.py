from django.contrib import admin
from chatbot.models import Chatbot

class ChatbotAdmin(admin.ModelAdmin):
        list_display = ('receiver','sender','message','created', 'chat_image')

admin.site.register(Chatbot, ChatbotAdmin)

# class SuggestionAdmin(admin.ModelAdmin):
#         list_display = ('by','description','datetime')

# admin.site.register(Suggestions, SuggestionAdmin)

