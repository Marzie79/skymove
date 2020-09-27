from django.contrib import admin
from home.models import *


@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)


@admin.register(HomeVideo)
class HomeVideoAdmin(admin.ModelAdmin):
    list_display = ('date',)
    readonly_fields = ('date',)
    search_fields = ('date',)


class PictureAdminInline(admin.TabularInline):
    model = ABoutUsHomeSlideShow


@admin.register(ABoutUsHome)
class ABoutUsHomeAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'date')
    readonly_fields = ('date',)
    list_display = ('title', 'date',)
    inlines = (PictureAdminInline,)


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    fields = (
        'phone_number', 'email', 'whats_app_phone_number', 'twitter', 'medium', 'facebook', 'telegram', 'instagram')
    list_display = ('phone_number', 'email',)
    search_fields = ('phone_number', 'email',)
