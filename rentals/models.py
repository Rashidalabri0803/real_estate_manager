from django.db import models

from properties.models import Property
from tenants.models import Tenant

class Rental(models.Model):
    RENTAL_STATUS_CHOICES = [('active','نشط'),('expired','منتهي'),]
    property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name="العقار")
    tenants = models.ForeignKey(Tenant, on_delete=models.CASCADE, verbose_name="المستأجر")
    rent_start = models.DateField(verbose_name="تاريخ بدء الايجار" )
    rent_end = models.DateField(verbose_name="تاريخ انتهاء الايجار" )
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="مبلغ الايجار")
    status = models.CharField(max_length=10, choices= RENTAL_STATUS_CHOICES, default='active', verbose_name="حالة الايجار")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الانشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="اخر تعديل")
    
    def __str__(self):
        return f"إيجار {self.property} - {self.tenant} ({self.get_status_display()})"
        
    class Meta:
        verbose_name = "ايجار"
        verbose_name_plural = "الايجارات"
        ordering = ['-created_at']
