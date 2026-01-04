from django.db import models
from django.conf import settings
from .utils import generate_wallet_address

User = settings.AUTH_USER_MODEL
# Create your models here.

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wallet')
    wallet_address = models.CharField(max_length=255, unique=True, default=generate_wallet_address, editable=False)
    balance = models.DecimalField(max_digits=12, decimal_places=8, default=0)

    def __str__(self):
        return f"{self.user} - {self.wallet_address}"