from django.contrib import admin
from app_general.models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'desc', 'phonenumber']
    search_fields = ['name', 'email']

admin.site.register(Contact, ContactAdmin)