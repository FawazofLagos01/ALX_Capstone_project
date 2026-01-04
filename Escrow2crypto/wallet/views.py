from decimal import InvalidOperation
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Wallet
from .serializers import WalletSerializer
from rest_framework import status
from decimal import Decimal
# Create your views here.

class WalletBalanceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
            wallet, _ = Wallet.objects.get_or_create(user=request.user)
            serializer = WalletSerializer(wallet)
            return Response(serializer.data, status=200)

class DepositView(APIView):
    """
    Deposit funds into the user's wallet.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            amount = Decimal(request.data.get('amount'))
        except (TypeError, InvalidOperation):
            return Response({'error': 'Invalid amount'}, status=400)
        
        if amount <= 0:
            return Response({'error': 'Deposit amount must be greater than zero'}, status=400)
        
        wallet, _ = Wallet.objects.get_or_create(user=request.user)
        wallet.balance += float(amount)
        wallet.save()
        return Response({'message': 'Deposit successful', 'new_balance': wallet.balance}, status=200)
    

class WithdrawView(APIView):
    """
    Withdraw funds from the user's wallet.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            amount = Decimal(request.data.get('amount'))
        except (TypeError, InvalidOperation):
            return Response({'error': 'Invalid amount'}, status=400)
        
        if amount <= 0:
            return Response({'error': 'Withdrawal amount must be greater than zero'}, status=400)
        
        wallet, _ = Wallet.objects.get_or_create(user=request.user)
        if wallet.balance < amount:
            return Response({'error': 'Insufficient balance'}, status=400)
        
        wallet.balance -= float(amount)
        wallet.save()
        return Response({'message': 'Withdrawal successful', 'new_balance': wallet.balance}, status=200)