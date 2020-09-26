from django.contrib import admin
from home.models import *


@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    search_fields = ('email',)


@admin.register(HomeVideo)
class HomeVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'date')
    readonly_fields = ('date',)
    search_fields = ('date',)


class PictureAdminInline(admin.TabularInline):
    model = ABoutUsHomeSlideShow


@admin.register(ABoutUsHome)
class ClassAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'date')
    readonly_fields = ('date',)
    list_display = ('title', 'date',)
    inlines = (PictureAdminInline,)
