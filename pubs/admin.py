from django.contrib import admin
from pubs.models import Publication

class PublicationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Options', {'fields': ['featured']}),
        ('CALM fields', {'fields': ['id', 'title', 'authors', 'year', 'summary'], 'classes': ['collapse']}),
    ]
    list_display = ['title', 'year', 'featured']
    list_filter = ['featured']
    search_fields = ['title']

admin.site.register(Publication,PublicationAdmin)
