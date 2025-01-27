from django.urls import path
from . import views

urlpatterns = [
    path('wallet/', views.WalletCreateListView.as_view(), name='wallet-create-list'),
    path('wallet/<int:pk>/', views.WalletRetrieveUpdateDestroyView.as_view(), name='wallet-detail-view'),
    path('transaction/', views.TransactionCreateListView.as_view(), name='transaction-create-list'),
    path('transaction/<int:pk>/', views.TransactionRetrieveDestroyView.as_view(), name='transaction-detail-view'),
]