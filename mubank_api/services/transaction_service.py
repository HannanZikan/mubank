from mubank_api.models import Transaction
from mubank_api.serializers import TransactionSerializer

class TransactionService:

    def create_transaction(transaction_serializer: TransactionSerializer):
        new_transaction = transaction_serializer
        new_transaction.save()
    