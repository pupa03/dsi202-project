from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app_users.models import CustomUser, Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']



admin.site.register(CustomUser, UserAdmin)
admin.site.register(Profile, ProfileAdmin)