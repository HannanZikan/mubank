from rest_framework import serializers
from mubank_api.models import Wallet, Transaction
from django.contrib.auth.models import User

class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
