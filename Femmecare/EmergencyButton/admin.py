from django.contrib import admin
from EmergencyButton.models import EmergencyButton

class EmergencyButtonAdmin(admin.ModelAdmin):
    list_display=('id', 'message', 'sent_to')


admin.site.register(EmergencyButton, EmergencyButtonAdmin)