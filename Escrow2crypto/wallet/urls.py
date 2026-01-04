from django.urls import path
from .views import WalletBalanceView

urlpatterns = [
    path('wallet/balance/', WalletBalanceView.as_view(), name='wallet-balance'),
    path('wallet/deposit/', WalletBalanceView.as_view(), name='wallet-deposit'),
    path('wallet/withdraw/', WalletBalanceView.as_view(), name='wallet-withdraw'),
]