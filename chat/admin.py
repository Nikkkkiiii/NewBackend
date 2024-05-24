from django.contrib import admin
from .models import Messages

class ChatAdmin(admin.ModelAdmin):
    list_display = ('receiver','sender','message','created', 'chat_image')

admin.site.register(Messages, ChatAdmin)

# admin.site.register(Messages)