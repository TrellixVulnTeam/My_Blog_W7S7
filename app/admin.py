from django.contrib import admin
from .models import structure, comment


class structureAdmin(admin.ModelAdmin):
    list_display = ('title','published','status', )
    list_filter = ('created','published', 'status', )
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    #raw_id_fields = ('author', )
    date_hierarchy = 'published'
    ordering = ('published', 'status')


class commentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

admin.site.register(comment, commentAdmin)

admin.site.register(structure, structureAdmin)

