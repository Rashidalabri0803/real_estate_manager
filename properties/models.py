from django.db import models

# Create your models here.
class Property(models.Model):
    PROPERTY_STATUS = [('available','متاح'),('rented','مؤجر'),]
    PROPERTY_TYPE = [('residential','سكني'),('commercial','تجاري'),]
    name = models.CharField(max_length=100, verbose_name="اسم العقار")
    location = models.CharField(max_length=100, verbose_name="الموقع")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    description = models.TextField(verbose_name="الوصف")
    area = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="مساحة العقار بالمتر المربع")
    rooms = models.IntegerField(verbose_name="عدد الغرف")
    property_type = models.CharField(max_length=15, choices=PROPERTY_TYPE, verbose_name="نوع العقار")
    status = models.CharField(max_length=10, choices=PROPERTY_STATUS, default='available', verbose_name="الحالة")
    image = models.ImageField(upload_to='property_images/', null=True, blank=True, verbose_name="صورة العقار")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")
    
    def __str__(self):
        return f"{self.name}. {self.get_status_display()}"
