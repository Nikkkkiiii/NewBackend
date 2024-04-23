from django.contrib import admin
from map.models import MapMarker

class MapAdmin(admin.ModelAdmin):
    list_display = ('id' , 'longitude', 'latitude')

admin.site.register(MapMarker, MapAdmin)
