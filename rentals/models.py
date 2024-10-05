from django.db import models

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=1255)
    address = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Tenant(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Lease(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Lease for {self.property.name} - {self.tenant.first_name}"