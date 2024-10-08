from django import forms
from django.contrib.admin.options import widgets
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'location', 'price', 'description', 'area', 'rooms', 'property_type', 'status', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placholder': 'أدخل اسم العقار'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placholder': 'أدخل موقع العقار'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placholder': 'أدخل سعر العقار'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placholder': 'أدخل وصف العقار'}),
            'area': forms.NumberInput(attrs={'class': 'form-control', 'placholder': 'أدخل مساحة العقار'}),
            'rooms': forms.NumberInput(attrs={'class': 'form-control', 'placholder': 'أدخل عدد الغرف'}),
            'property_type': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }