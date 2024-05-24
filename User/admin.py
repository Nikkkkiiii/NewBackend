from django.contrib import admin
from .models import MobileTokens, User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'address', 'phone_number')
    search_fields = ('username', 'email')

admin.site.register(User, UserAdmin)

# class MobileTokenAdmin(admin.ModelAdmin):
#     list_display= ('phone_key', 'device_name', 'user', 'is_logged_in')


# admin.site.register(MobileTokens, MobileTokenAdmin)