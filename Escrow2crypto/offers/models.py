from django.db import models
from users.models import User

# Create your models here.

class Offer(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    gift_card_type = models.CharField(max_length=100)
    login_email = models.CharField(max_length=255)
    login_password = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=12, decimal_places=8)
    status = models.CharField(max_length=50, default='active')