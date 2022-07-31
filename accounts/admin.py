from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from accounts.forms import (OnlinevoteUserChangeForm, OnlinevoteUserCreationForm)
from accounts.models import OnlinevoteUser, RegisteredVoters, Year, School, Department, AspirantPosition


class OnlinevoteUserAdmin(UserAdmin):
    add_form = OnlinevoteUserCreationForm
    form = OnlinevoteUserChangeForm
    model = OnlinevoteUser
    filter_horizontal = ('user_permissions',)
    list_display = ('email', 'id', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Profile', {'fields': ('first_name', 'last_name', 'email_verified',)}),
        ('Activity History', {'fields': ('date_joined',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active',)}
         ),
    )

    search_fields = ('email', 'fist_name', 'last_name',)
    ordering = ('email',)
    list_per_page = 50


class OnlinevotersAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'email', 'name', 'matric', 'aspirant', 'department', 'year', 'verified_voter']
    search_fields = ['email', 'department', 'matric', 'aspirant', 'verified_voter', 'department']
    list_display_links = ['email']
    list_per_page = 50


class YearAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'year']
    list_display_links = ['year']
    list_per_page = 50


class SchoolAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'school']
    list_display_links = ['school']
    list_per_page = 50


class DepartmentAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'department']
    list_display_links = ['department']
    list_per_page = 50


class AspirantPositionAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'department', 'position', 'position_type']
    list_display_links = ['department']
    list_per_page = 50


admin.site.unregister(Group)
admin.site.register(OnlinevoteUser, OnlinevoteUserAdmin)
admin.site.register(RegisteredVoters, OnlinevotersAdmin)
admin.site.register(Year, YearAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(AspirantPosition, AspirantPositionAdmin)

# Customize Admin Portal Name
admin.site.site_header = "ONLINE VOTING Administration"
admin.site.site_title = "ONLINE VOTING Admin Portal"
admin.site.index_title = "Welcome to ONLINE VOTING Server Administration Portal"
