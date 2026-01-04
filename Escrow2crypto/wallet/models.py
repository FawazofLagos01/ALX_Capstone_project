from django.db import models
from django.conf import settings

# Create your models here.

class Wallet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    usdt_balance = models.DecimalField(max_digits=12, decimal_places=8, default=0)

    def __str__(self):
        return f"{self.user.username} Wallet"