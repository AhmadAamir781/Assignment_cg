
from django.urls import path
from .views import PostTransactionView,RetrieveUserTransactionsByTimestampView
urlpatterns = [
    path('Transactions/', PostTransactionView.as_view(), name="transactions"),
    path('Transactions/<int:user_id>/', PostTransactionView.as_view(), name="transactionsUser"),
    path('Transactions/<int:user_id>/<str:start_timestamp>/<str:end_timestamp>/', RetrieveUserTransactionsByTimestampView.as_view(), name="rUsertransbytime"),
]
    