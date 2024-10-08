from django import forms
from .models import Tenant

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'email', 'phone', 'address', 'id_number']