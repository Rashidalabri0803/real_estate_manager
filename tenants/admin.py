from django.contrib import admin
from .models import Tenant
# Register your models here.

class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'id_number', 'address', 'profession', 'registration_date')
    list_filter = ('registration_date',)
    search_fields = ('name', 'email', 'phone', 'id_number')
    ordering = ('-registration_date',)

admin.site.register(Tenant, TenantAdmin)