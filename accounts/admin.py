from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserChangeForm, UserCreationForm
from .models import *


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = (
        '__str__', 'nationality', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {
            'fields': (
                'validation', 'first_name', 'last_name', 'nationality', 'phone_number', 'email', 'company_name',
                'password')
        }),
        ('Permission', {'fields': ('is_admin', 'is_active', 'is_validate')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('nationality',)
    ordering = ('nationality',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
