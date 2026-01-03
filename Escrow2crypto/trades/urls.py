from django.urls import path
from .views import StartTradeView, TradeStatusView

urlpatterns = [
    path('trades/start/', StartTradeView.as_view(), name='start-trade'),
    path('trades/<int:trade_id>/status/', TradeStatusView.as_view(), name='trade-status'),
]