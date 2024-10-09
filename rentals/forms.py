from django import forms
from .models import Rental

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['property', 'start_date', 'end_date', 'payment_status', 'monthly_rent',  'contract_status']
        widgets = {
            'property' : forms.Select(attrs={'class': 'form-control'}),
            #'tenant' : forms.Select(attrs={'class': 'form-control'}),
            'start_date' : forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'end_date' : forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'monthly_rent' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أدخل سعر الإجرة الشهري'}),
            'payment_status' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            #'next_due_date' : forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'contract_status' : forms.Select(attrs={'class': 'form-control'}),
        }