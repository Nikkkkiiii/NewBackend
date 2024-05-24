# mapapp/admin.py
from django.contrib import admin
from .models import Hospital

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'address', 'city')
    search_fields = ('name', 'address', 'city')
