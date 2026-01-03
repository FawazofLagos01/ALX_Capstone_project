from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Offer
from .serializers import OfferSerializer, CreateOfferSerializer

# Create your views here.

class CreateOfferView(APIView):
    def post(self, request):
        if request.user.role != 'seller':
            return Response({'error': 'Only sellers can create offers.'}, status=status.HTTP_403_FORBIDDEN)
        
        selferializer = CreateOfferSerializer(data=request.data)
        if selferializer.is_valid():
            selferializer.save(seller=request.user)
            return Response(selferializer.data, status=status.HTTP_201_CREATED)
        
        return Response(selferializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ListOffersView(APIView):
    def get(self, request):
        offers = Offer.objects.filter(status='active')
        serializer = OfferSerializer(offers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)