from django.db import models
from properties.models import Property
from tenants.models import Tenant

class Rental(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenants = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"إيجار {self.property} للمستأجر {self.tenant}"