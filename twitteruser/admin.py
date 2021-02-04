from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
# from .models import TwitterUser,TwitterFollowers
from .models import TwitterUser

# admin.site.register(TwitterFollowers)
class CustomUserAdmin(UserAdmin):
    model = TwitterUser

admin.site.register(TwitterUser, CustomUserAdmin)
