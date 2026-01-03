from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Trade, Escrow
from offers.models import Offer
from wallet.models import Wallet
from decimal import Decimal

# Create your views here.

class StartTradeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        buyer = request.user
        offer_id = request.data.get('offer_id')
        amount = request.data.get('amount')

        offer = Offer.objects.get(id=offer_id)
        amount = Decimal(request.data.get('amount'))

        offer = Offer.objects.get(id=offer_id)
        seller_wallet = Wallet.objects.get(user=offer.seller)

        if seller_wallet.usdt_balance < amount:
            return Response({'error': 'Seller does not have enough USDT balance.'}, status=400)
        
        seller_wallet.usdt_balance -= amount
        seller_wallet.save()

        trade = Trade.objects.create(
            buyer=request.user,
            offer=offer,
            amount=amount,
            usdt_locked=amount,
            status='pending'
        )

        Escrow.objects.create(
            trade=trade,
            locked_usdt=amount,
            released=False
        )

        return Response({'message': 'Trade started successfully.', 'trade_id': trade.id}, status=201)
    

class TradeStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, trade_id):
        trade = Trade.objects.get(id=trade_id, buyer=request.user)
        return Response({
            'status': trade.status,
            'evidence': trade.evidence_img.url if trade.evidence_img else None
        })
