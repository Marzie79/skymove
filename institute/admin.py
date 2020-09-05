from django.contrib import admin
from .models import *


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number', 'message')
    search_fields = ('name',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'counter', 'date')
    search_fields = ('date',)


@admin.register(Support)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone_number', 'date')
    search_fields = ('date',)
