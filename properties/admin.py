from django.contrib import admin
from .models import Property
# Register your models here.
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price', 'property_type', 'status', 'created_at')
    list_filter = ('status', 'property_type', 'location')
    search_fields = ('name', 'location')
    list_editable = ('status',)
    ordering = ('-created_at',)
  
admin.site.register(Property, PropertyAdmin)