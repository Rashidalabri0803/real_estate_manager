from django import forms
from django.contrib.admin.options import widgets
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'price', 'description', 'area', 'property_type', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placholder': 'أدخل اسم العقار'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placholder': 'أدخل سعر العقار'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'area': forms.NumberInput(attrs={'class': 'form-control', 'placholder': 'أدخل مساحة العقار'}),
            'property_type': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
