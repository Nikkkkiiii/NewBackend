from django.contrib import admin
from notification.models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'message', 'user')

admin.site.register(Notification, NotificationAdmin)
