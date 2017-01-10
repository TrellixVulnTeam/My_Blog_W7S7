from django.contrib import admin
from .models import structure


class structureAdmin(admin.ModelAdmin):
    list_display = {'title','published'}
    list_filter = {'created','publish'}
    search_fields = {'title', 'body'}
    prepopulated_fields = {'slug':('title')}
    raw_id_fields = 'author'
    date_hierarchy = 'published'
    ordering = ['published']




admin.site.register(structure)

