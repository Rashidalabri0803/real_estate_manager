from django.shortcuts import render, redirect, get_object_or_404
from .models import Property
from .forms import PropertyForm
# Create your views here.
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'properties/property_list.html', {'properties': properties})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'properties/property_detail.html', {'property': property})

def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'properties/property_form.html', {'form': form})

def property_update(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_detail', pk=pk)
    else:
        form = PropertyForm(instance=property)
    return render(request, 'properties/property_form.html', {'form': form})

def property_delete(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.metho == 'POST':
        property.delete()
        return redirect('property_list')
    return render(request, 'properties/property_confirm_delete.html', {'property': property})