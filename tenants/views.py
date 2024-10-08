from django.shortcuts import render
from .models import Tenant
# Create your views here.
def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenants/tenant_list.html', {'tenants': tenants})