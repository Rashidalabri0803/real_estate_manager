from django.db import models
from properties.models import Property
# Create your models here.
class Rental(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.tenant_name} - {self.property.title}"