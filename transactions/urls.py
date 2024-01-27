
from django.urls import path
from .views import TransactionView,RetrieveUserTransactionsByTimestampView
urlpatterns = [
    path('transactions/', TransactionView.as_view(), name="transactions"),
    path('transactions/<int:user_id>/', TransactionView.as_view(), name="transactionsUser"),
    path('transactions/<int:user_id>/<str:start_timestamp>/<str:end_timestamp>/', RetrieveUserTransactionsByTimestampView.as_view(), name="rUsertransbytime"),
]
    