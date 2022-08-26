from django.contrib import admin
from .models import VotersModel, VoteModel


class VotersAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'choice', 'department', 'year', 'created_by']
    list_display_links = ['choice']
    list_per_page = 50


class VoteAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'department', 'start', 'end', 'year']
    list_display_links = ['department']
    list_per_page = 50


admin.site.register(VoteModel, VoteAdmin)
admin.site.register(VotersModel, VotersAdmin)
