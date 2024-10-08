from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Tenant

@receiver(post_save, sender=Tenant)
def send_tenant_email(sender, instance, created, **kwargs):
    if created:
       send_mail(
           'مرحبا بك في نظام إدارة العقارات',
           f'مرحباً {instance.name}, شكرا لانضمامك',
           'admin.realestate.com',
           [instance.email],
           fail_silently=False,
       )