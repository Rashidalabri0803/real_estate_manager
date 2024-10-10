from django.contrib import admin
from .models import Rental
# Register your models here.
class RentalAdmin(admin.ModelAdmin):
    list_display = ('property', 'tenants', 'rent_start', 'rent_end', 'rent_amount', 'status', 'created_at')
    list_filter = ('status', 'rent_start', 'rent_end')
    search_fields = ('property__name', 'tenant__name')
    readonly_fields = ('created_at','updated_at')
    
admin.site.register(Rental, RentalAdmin)
