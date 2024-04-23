from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'address', 'phone_number')
    search_fields = ('username', 'email')

admin.site.register(User, UserAdmin)