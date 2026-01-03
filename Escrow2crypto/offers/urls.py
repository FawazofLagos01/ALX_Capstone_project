from django.urls import path
from .views import CreateOfferView, ListOffersView

urlpatterns = [
    path('offers/create/', CreateOfferView.as_view(), name='create-offer'),
    path('offers/', ListOffersView.as_view(), name='list-offers'),
]