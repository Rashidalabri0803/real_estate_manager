from django.db import models

# Create your models here.
class Tenant(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    id_number = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name