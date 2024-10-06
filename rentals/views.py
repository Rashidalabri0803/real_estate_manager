from django.shortcuts import render, get_object_or_404
from .models import Property, Tenant, Lease
# Create your views here.
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'property_detail.html', {'property': property})