from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Company, Employee

User = get_user_model()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if instance.type == "Company" and created:
        Company.objects.create(user=instance)
    else:
        Employee.objects.create(user=instance)
