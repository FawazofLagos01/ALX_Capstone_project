from rest_framework import serializers
from .models import Offer

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = [ 'id', 'seller', 'gift_card_type', 'login_email', 'login_password', 'rate', 'status', 'created_at' ]

class CreateOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = [ 'seller', 'gift_card_type', 'login_email', 'login_password', 'rate' ]