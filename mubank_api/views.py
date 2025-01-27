from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from mubank_api.models import Wallet, Transaction
from mubank_api.serializers import WalletSerializer, TransactionSerializer
from mubank_api.services import WalletService

class WalletCreateListView(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class WalletRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class TransactionView(APIView):

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            transaction = serializer.data            
            WalletService.increment_balance(transaction['receiving_wallet_id'],transaction['ammount'])
            return Response(transaction, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionListView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
