from django.contrib import admin
from chatbot.models import Chatbot

class ChatbotAdmin(admin.ModelAdmin):
        list_display = ('sendTo','sendFrom','message','datetime')

admin.site.register(Chatbot, ChatbotAdmin)

