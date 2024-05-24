# admin.py
from django.contrib import admin
from .models import Emergency

class EmergencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message', 'location', 'timestamp')
    search_fields = ('user__username', 'message', 'location')

admin.site.register(Emergency, EmergencyAdmin)
