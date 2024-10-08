from django import forms
from .models import Rental

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['property', 'tenant', 'start_date', 'end_date', 'payment_status', 'monthly_rent']