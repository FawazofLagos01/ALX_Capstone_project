from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Wallet
from .serializers import WalletSerializer

# Create your views here.

class WalletBalanceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
            wallet, _ = Wallet.objects.get_or_create(user=request.user)
            serializer = WalletSerializer(wallet)
            return Response(serializer.data, status=200)