from django.contrib import admin
from documentary.models import Author, Title, Site


class AuthorAdmin(admin.ModelAdmin):
    """docstring for AuthorAdmin"""
    list_display = ('name', 'email', 'website')
    search_fields = ('name',)

class TitleAdmin(admin.ModelAdmin):
    """docstring for TitleAdmin"""
    list_display = ('title_name',)
    search_fields = ('title_name',)


class SiteAdmin(admin.ModelAdmin):
    """docstring for SiteAdmin"""
    list_display = ('id','title','author', 'create_time')
    list_filter = ('create_time',)
    date_hierarchy = 'create_time'
    ordering = ('-create_time',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Site,SiteAdmin)