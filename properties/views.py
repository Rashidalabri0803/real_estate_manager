from django.shortcuts import render
from .models import Property
# Create your views here.
def index(request):
    properties = Property.objects.all()
    return render(request, 'properties/index.html', {'properties': properties})