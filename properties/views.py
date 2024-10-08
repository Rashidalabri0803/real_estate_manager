from django.shortcuts import render, redirect, get_object_or_404
from .models import Property
from .forms import PropertyForm
# Create your views here.

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'properties/property_list.html', {'properties': properties})

def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'properties/add_property.html', {'form': form})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'properties/property_detail.html', {'property': property})

def searched_properties(request):
    query = request.GET.get('q')
    properties = Property.objects.filter(name__icontains=query)
    return render(request, 'properties/property_list.html', {'properties': properties})