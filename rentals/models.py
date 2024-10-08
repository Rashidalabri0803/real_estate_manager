from django.db import models

from properties.models import Property
from tenants.models import Tenant

class Rental(models.Model):
    CONTRACT_STATUS = [('active','مفعل'),('expired','منتهي'),]
    property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name="العقار")
    tenants = models.ForeignKey(Tenant, on_delete=models.CASCADE, verbose_name="المستأجر")
    start_date = models.DateField(verbose_name="تاريخ البدء" )
    end_date = models.DateField(verbose_name="تاريخ النهاية" )
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="الايجار الشهرية")
    payment_status = models.BooleanField(default=False, verbose_name="حالة الدفع")
    next_payment_due = models.DateField(verbose_name="تاريخ الدفع القادمة" )
    contract_status = models.CharField(max_length=20, choices=[('active', 'فعال'), ('terminated', 'منتهي')], default='active', verbose_name="حالة العقد")
    
    def __str__(self):
        return f"إيجار {self.property.name} للمستأجر {self.tenant.name}"
