from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import customUser

class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'user_type', 'first_name', 'last_name', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('User Type', {'fields': ('user_type',)}), 
        ('Otp', {'fields':('otp',)}), # Add user_type to the fieldsets
    )
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

admin.site.register(customUser, CustomUserAdmin)
