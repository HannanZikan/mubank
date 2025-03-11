from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.UserCreateView.as_view(), name='user-create'),
    path('wallet/', views.WalletCreateListView.as_view(), name='wallet-create-list'),
    path('wallet/<int:pk>/', views.WalletRetrieveUpdateDestroyView.as_view(), name='wallet-detail-view'),
    path('transaction/', views.TransactionListView.as_view(), name='transaction-list-list'),
    path('transaction/deposit', views.TransactionDepositView.as_view(), name='transaction-deposit-view'),
    path('transaction/withdrawal', views.TransactionWithdrawalView.as_view(), name='transaction-withdrawal-view'),
    path('transaction/transfer', views.TransactionTransferView.as_view(), name='transaction-transfer-view'),
    path('transaction/<int:pk>/', views.TransactionRetrieveDestroyView.as_view(), name='transaction-delete-view'),
]