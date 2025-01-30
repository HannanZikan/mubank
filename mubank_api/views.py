from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.dateparse import parse_date
from django.contrib.auth.models import User, Group
from mubank_api.models import Wallet, Transaction
from mubank_api.serializers import WalletSerializer, TransactionSerializer, UserSerializer
from mubank_api.services import WalletService, TransactionService

class WalletCreateListView(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class WalletRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class TransactionDepositView(APIView):

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            TransactionService.create_transaction(serializer)
            transaction = serializer.data            
            WalletService.increment_balance(transaction['receiving_wallet_id'],transaction['ammount'])
            return Response(transaction, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TransactionWithdrawalView(APIView):

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            TransactionService.create_transaction(serializer)
            transaction = serializer.data            
            WalletService.decrement_balance(transaction['transfer_wallet_id'],transaction['ammount'])
            return Response(transaction, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TransactionTransferView(APIView):

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            TransactionService.create_transaction(serializer)
            transaction = serializer.data            
            WalletService.decrement_balance(transaction['transfer_wallet_id'],transaction['ammount'])
            WalletService.increment_balance(transaction['receiving_wallet_id'],transaction['ammount'])
            return Response(transaction, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionListView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if start_date:
            start_date = parse_date(start_date)
            queryset = queryset.filter(created_at__gte=start_date)

        if end_date:
            end_date = parse_date(end_date)
            queryset = queryset.filter(created_at__lte=end_date)

        return queryset

class TransactionRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class UserCreateView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            new_user = User.objects.create_user(
                username = serializer.data['username'],
                password = serializer.data['password']
            )
            new_user.groups.add(Group.objects.get(name='user_default_permissions'))
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
