from django.db import models

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('apartment', 'شقة'),
        ('shop', 'محل'),
        ('office', 'مكتب'),
    ]
    STATUS_CHOICES = [
        ('available', 'متاح'),
        ('rented', 'مؤجر'),
        ('maintenance', 'تحت الصيانة'),
    ]

    name = models.CharField(max_length=200, verbose_name="اسم العقار")
    address = models.CharField(max_length=300, verbose_name="عنوان العقار")
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, default="apartment", verbose_name="نوع العقار")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    area = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="المساحة (م²)")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available', verbose_name="الحالة")
    description = models.TextField(blank=True, null=True, verbose_name="الوصف")
    image = models.ImageField(upload_to='properties/', blank=True, null=True, verbose_name="صورة العقار")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التعديل")
    
    def __str__(self):
        return f"{self.name} - {self.get_property_type_display()} - {self.address}"
        
    class Meta:
        verbose_name = "عقار"
        verbose_name_plural = "العقارات"
        ordering =['-created_at']
