from django.shortcuts import render, get_object_or_404
from .models import Property, Tenant, Lease
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, Permission
# Create your views here.
@login_required
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'property_detail.html', {'property': property})

@permission_required('rentals.change_propery')
def edite_property(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'edite_property.html', {'property': property})

