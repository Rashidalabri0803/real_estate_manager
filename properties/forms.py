from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'location', 'price', 'description', 'area', 'rooms', 'status']