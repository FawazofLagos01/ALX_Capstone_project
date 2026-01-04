from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Trade, Escrow
from offers.models import Offer
from wallet.models import Wallet
from decimal import Decimal
from .permissions import IsAdminUserOnly

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
        seller_wallet, _ = Wallet.objects.get_or_create(user=offer.seller)

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
    
class CompleteTradeView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUserOnly]

    def post(self, request, trade_id):
        trade = Trade.objects.get(id=trade_id, status='pending')
        escrow = Escrow.objects.get(trade=trade)

        buyer_wallet, _ = Wallet.objects.get_or_create(user=trade.buyer)

        #release USDT to buyer
        buyer_wallet.usdt_balance += escrow.locked_usdt
        buyer_wallet.save()

        escrow.released = True
        escrow.save()

        trade.status = 'completed'
        trade.save()

        return Response({'message': 'Trade completed and USDT released to buyer.'}, status=200)
    
class FailTradeView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUserOnly]

    def post(self, request, trade_id):
        trade = Trade.objects.get(id=trade_id, status='pending')
        escrow = Escrow.objects.get(trade=trade)

        seller_wallet, _ = Wallet.objects.get_or_create(user=trade.offer.seller)

        #return USDT to seller
        seller_wallet.usdt_balance += escrow.locked_usdt
        seller_wallet.save()

        escrow.released = True
        escrow.save()

        trade.status = 'failed'
        trade.evidence_img = request.data.get('evidence_img')
        trade.save()

        return Response({'message': 'Trade failed and USDT returned to seller, Proof sent to buyer!.'}, status=200)