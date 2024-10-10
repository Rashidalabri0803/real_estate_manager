from django.contrib import admin
from .models import Property

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'property_type', 'status')
    search_fields = ('name', 'property_type', 'status')
    list_filter = ('status', 'property_type')

admin.site.register(Property, PropertyAdmin)
