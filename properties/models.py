from django.db import models

# Create your models here.
class Property(models.Model):
    PROPERTY_STATUS = [('available','متاح'),('rented','مؤجر'),]
    PROPERTY_TYPE = [('residential','سكني'),('commercial','تجاري'),]
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    area = models.DecimalField(max_digits=7, decimal_places=2, help_text="مساحة العقار بالمتر المربع")
    rooms = models.IntegerField()
    property_type = models.CharField(max_length=15, choices=PROPERTY_TYPE)
    status = models.CharField(max_length=10, choices=PROPERTY_STATUS, default='available')
    image = models.ImageField(upload_to='property_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}. {self.get_status_display()}"
