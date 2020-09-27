from django.contrib import admin
from .models import *


@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'message', 'check')
    search_fields = ('name', 'email',)
    list_filter = ('check',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    fields = ('title', 'description', 'image', 'date')
    readonly_fields = ('date',)
    search_fields = ('title',)


@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'active')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'image')
    list_display = ('title',)


@admin.register(ABoutUs)
class ABoutUsAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'image', 'active')
    list_display = ('title', 'active')
