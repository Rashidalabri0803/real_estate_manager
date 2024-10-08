from django import forms
from .models import Tenant

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'email', 'phone', 'address', 'id_number', 'id_number', 'profession']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placholder': 'أدخل اسم العقار'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placholder': 'أدخل البريد الإلكتروني'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placholder': 'أدخل رقم الهاتف'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placholder': 'أدخل عنوان العقار'}),
            'id_number': forms.NumberInput(attrs={'class': 'form-control', 'placholder': 'أدخل رقم الهوية'}),
            'profession': forms.TextInput(attrs={'class': 'form-control', 'placholder': 'أدخل مهنة العقار'}),
        }