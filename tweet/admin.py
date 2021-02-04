from django.contrib import admin

# from django.contrib.auth.admin import UserAdmin
from .models import Tweet

admin.site.register(Tweet)

