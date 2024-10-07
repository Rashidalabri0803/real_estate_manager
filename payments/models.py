from django.db import models
from rentals.models import Rental
# Create your models here.
class Payment(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    amounrt = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Payment of {self.amount} for {self.rental.tenant_name}"