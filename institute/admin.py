from django.contrib import admin
from .models import *


@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number', 'message')
    search_fields = ('name',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')
    fields = ('title', 'description', 'image', 'date')
    readonly_fields = ('date',)
    search_fields = ('date',)


@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone_number', 'date')
    readonly_fields = ('date',)
    search_fields = ('date',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'image')
    list_display = ('id', 'title')


@admin.register(ABoutUs)
class ABoutUsAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'image', 'date')
    readonly_fields = ('date',)
    list_display = ('date',)
