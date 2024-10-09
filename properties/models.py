from django.db import models

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('apartment', 'شقة'),
        ('house', 'منزل'),
        ('office', 'مكتب'),
        ('land', 'أرض'),
    ]
    STATUS_CHOICES = [
        ('available', 'متاح'),
        ('rented', 'مؤجر'),
        ('sold', 'مباع'),
    ]

    name = models.CharField(max_length=100, verbose_name="اسم العقار")
    description = models.TextField(verbose_name="الوصف")
    location = models.CharField(max_length=200, verbose_name="الموقع")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, verbose_name="نوع العقار")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available', verbose_name="الحالة")
    area = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="المساحة (م²)")
    rooms = models.PositiveIntegerField(verbose_name="عدد الغرف")

    def __str__(self):
        return self.name
