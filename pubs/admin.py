from django.contrib import admin
from pubs.models import Publication, Line

class PublicationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Options', {'fields': ['has_fulltext', 'featured']}),
        ('CALM fields', {'fields': ['id', 'title', 'authors', 'year', 'summary'], 'classes': ['collapse']}),
    ]
    list_display = ['title', 'year', 'has_fulltext', 'featured']
    list_filter = ['has_fulltext', 'featured']
    search_fields = ['title']

admin.site.register(Publication,PublicationAdmin)
