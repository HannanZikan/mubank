from django.contrib import admin
from mubank_api import models

class WalletAdmin(admin.ModelAdmin):
    list_display = ('user_id','name','balance','created_at','updated_at')
    search_fields = ('user_id','name')
    list_filter = ['user_id']

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transfer_wallet_id','receiving_wallet_id','ammount','created_at','updated_at',)
    search_fields = ('transfer_wallet_id','receiving_wallet_id')

admin.site.register(models.Wallet, WalletAdmin)
admin.site.register(models.Transaction, TransactionAdmin)
