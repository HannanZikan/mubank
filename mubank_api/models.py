from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    transfer_wallet_id = models.ForeignKey(Wallet, related_name='transfer', on_delete=models.PROTECT)
    receiving_wallet_id = models.ForeignKey(Wallet, related_name='receiver', on_delete=models.PROTECT)
    value = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
