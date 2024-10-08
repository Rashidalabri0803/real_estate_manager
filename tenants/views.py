from django.shortcuts import render, redirect, get_object_or_404
from .models import Tenant
from .forms import TenantForm
# Create your views here.
def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenants/tenant_list.html', {'tenants': tenants})

def tenant_detail(request, pk):
    tenant = get_object_or_404(Tenant, pk=pk)
    return render(request, 'tenants/tenant_detail.html', {'tenant': tenant})

def tenant_create(request):
    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tenant_list')
    else:
        form = TenantForm()
    return render(request, 'tenants/tenant_form.html', {'form': form})

def tenant_update(request, pk):
    tenant = get_object_or_404(Tenant, pk=pk)
    if request.method == 'POST':
        form = TenantForm(request.POST, instance=tenant)
        if form.is_valid():
            form.save()
            return redirect('tenant_list')
    else:
        form = TenantForm(instance=tenant)
    return render(request, 'tenants/tenant_form.html', {'form': form})

def tenant_delete(request, pk):
    tenant = get_object_or_404(Tenant, pk=pk)
    if request.method == 'POST':
        tenant.delete()
        return redirect('tenant_list')
    return render(request, 'tenants/tenant_confirm_delete.html', {'tenant': tenant})