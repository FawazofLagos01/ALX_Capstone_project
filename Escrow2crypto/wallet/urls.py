from django.urls import path
from .views import WalletBalanceView

urlpatterns = [
    path('balance/', WalletBalanceView.as_view(), name='wallet-balance'),
]