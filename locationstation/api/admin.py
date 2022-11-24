from django.contrib import admin
from .models import Listing

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin



@admin.register(Listing)
class ListingAdmin(ImportExportModelAdmin):
    fields = (
        'neighbourhood_group', 'neighbourhood', 
        'latitude','longitude','price',
        'created_at'
    )
    list_display = ('neighbourhood_group', 'neighbourhood', 
        'latitude','longitude','price',
        'created_at')
    search_fields = ('neighbourhood_group',)
