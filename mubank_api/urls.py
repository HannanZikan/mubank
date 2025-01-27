from django.urls import path
from . import views

urlpatterns = [
    path('wallet/', views.WalletCreateListView.as_view(), name='wallet-create-list'),
    path('wallet/<int:pk>/', views.WalletRetrieveUpdateDestroyView.as_view(), name='wallet-detail-view'),
    path('transaction/', views.TransactionListView.as_view(), name='transaction-list-list'),
    path('transaction/create', views.TransactionView.as_view(), name='transaction-create-view'),
    path('transaction/<int:pk>/', views.TransactionRetrieveDestroyView.as_view(), name='transaction-delete-view'),
]