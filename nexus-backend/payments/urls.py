from django.urls import path
from .views import DepositView, WithdrawView, TransferView, TransactionListView

urlpatterns = [
    path('deposit/', DepositView.as_view(), name='deposit'),
    path('withdraw/', WithdrawView.as_view(), name='withdraw'),
    path('transfer/', TransferView.as_view(), name='transfer'),
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
]
