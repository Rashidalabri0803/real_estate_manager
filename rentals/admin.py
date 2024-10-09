from django.contrib import admin
from .models import Rental
# Register your models here.
#class RentalAdmin(admin.ModelAdmin):
    #list_display = ('property', 'tenant', 'start_date', 'end_date', 'month_rent', 'contract_status', 'next_payment_due', 'payment_status')
    #list_filter = ('contract_status', 'payment_status', 'start_date', 'end_date')
    #search_fields = ('property__name', 'tenant__name')
    #ordering = ('-start_date',)
    
admin.site.register(Rental)
