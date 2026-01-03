from django.db import models
from users.models import User
from offers.models import Offer

class Trade(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('disputed', 'Disputed'),
    ]

    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=8)  # <-- fixed
    gift_card_code = models.CharField(max_length=255, blank=True, null=True)
    gift_card_image = models.ImageField(upload_to='cards/', blank=True, null=True)
    usdt_locked = models.DecimalField(max_digits=20, decimal_places=8)
    status = models.CharField(max_length=50, default='pending')
    evidence_img = models.ImageField(upload_to='evidence/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Escrow(models.Model):
    trade = models.OneToOneField(Trade, on_delete=models.CASCADE)
    locked_usdt = models.DecimalField(max_digits=20, decimal_places=8)
    released = models.BooleanField(default=False)


