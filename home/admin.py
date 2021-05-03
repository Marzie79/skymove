from django.contrib import admin
from home.models import *


@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)


@admin.register(HomeVideo)
class HomeVideoAdmin(admin.ModelAdmin):
    list_display = ('video', 'active')


class PictureAdminInline(admin.TabularInline):
    model = ABoutUsHomeSlideShow


@admin.register(ABoutUsHome)
class ABoutUsHomeAdmin(admin.ModelAdmin):
    fields = ('title', "title_fa",'description', "description_fa",'active')
    list_display = ('title', 'active',)
    inlines = (PictureAdminInline,)


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    fields = (
        'phone_number', 'email', 'whats_app_phone_number', 'twitter', 'medium', 'facebook', 'telegram', 'instagram', 'address', "address_fa" ,'map',
        'active')
    list_display = ('phone_number', 'email', 'active')
    search_fields = ('phone_number', 'email',)
