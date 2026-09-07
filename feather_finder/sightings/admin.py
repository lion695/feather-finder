from django.contrib import admin
from .models import BirdSpecies, Sighting

@admin.register(BirdSpecies)
class BirdSpeciesAdmin(admin.ModelAdmin):
    """
    Registers the BirdSpecies catalog structure within the Django Admin Panel.
    """
    list_display = ('common_name', 'scientific_name')
    search_fields = ['common_name', 'scientific_name']


@admin.register(Sighting)
class SightingAdmin(admin.ModelAdmin):
    """
    Registers custom user bird sightings logs with filters and sorting tools.
    """
    list_display = ('species', 'user', 'date_spotted', 'location_name', 'created_on')
    list_filter = ('date_spotted', 'species')
    search_fields = ['location_name', 'notes']
    date_hierarchy = 'date_spotted'
