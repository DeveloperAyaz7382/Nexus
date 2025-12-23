from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer

class DepositView(generics.CreateAPIView):
    serializer_class = TransactionSerializer

class WithdrawView(generics.CreateAPIView):
    serializer_class = TransactionSerializer

class TransferView(generics.CreateAPIView):
    serializer_class = TransactionSerializer

class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
