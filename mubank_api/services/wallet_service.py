from mubank_api.models import Wallet
from decimal import Decimal


class WalletService:

    @staticmethod
    def increment_balance(wallet_id, ammount):
        wallet = Wallet.objects.get(id = wallet_id)
        wallet.balance += Decimal(ammount)
        wallet.save()

    @staticmethod
    def decrement_balance(wallet_id, ammount):
        wallet = Wallet.objects.get(id = wallet_id)
        wallet.balance -= Decimal(ammount)
        wallet.save()
