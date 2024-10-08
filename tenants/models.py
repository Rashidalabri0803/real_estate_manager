from django.db import models

# Create your models here.
class Tenant(models.Model):
    name = models.CharField(max_length=100, verbose_name="الاسم")
    phone = models.CharField(max_length=15, verbose_name="رقم الهاتف")
    email = models.EmailField(verbose_name="البريد الالكتروني")
    id_number = models.CharField(max_length=20, unique=True, verbose_name="رقم الهوية")
    address = models.CharField(max_length=255, verbose_name="العنوان")
    profession = models.CharField(max_length=100, blank=True, verbose_name="الوظيفة")
    registration_date = models.DateField(auto_now_add=True, verbose_name="تاريخ التسجيل")
    
    def __str__(self):
        return self.name