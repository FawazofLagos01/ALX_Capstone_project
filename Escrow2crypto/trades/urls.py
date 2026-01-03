from django.urls import path
from .views import StartTradeView, TradeStatusView, CompleteTradeView, FailTradeView

urlpatterns = [
    path('trades/start/', StartTradeView.as_view(), name='start-trade'),
    path('trades/<int:trade_id>/status/', TradeStatusView.as_view(), name='trade-status'),
    path('trades/<int:trade_id>/complete/', CompleteTradeView.as_view(), name='complete-trade'),
    path('trades/<int:trade_id>/fail/', FailTradeView.as_view(), name='fail-trade'),
]