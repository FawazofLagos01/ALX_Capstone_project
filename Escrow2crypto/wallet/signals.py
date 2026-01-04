from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Wallet
from django.conf import settings
from django.apps import apps

User = apps.get_model(settings.AUTH_USER_MODEL)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)