from .models import *
from django.contrib import admin

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', "date")