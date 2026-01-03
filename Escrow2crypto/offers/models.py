from django.db import models
from users.models import User
from django.conf import settings

# Create your models here.

class Offer(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('completed', 'Completed'),
    ]

    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    gift_card_type = models.CharField(max_length=100)
    login_email = models.CharField(max_length=255)
    login_password = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=12, decimal_places=8)
    status = models.CharField(max_length=50, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Offer {self.id} by {self.seller.username} - {self.gift_card_type}"