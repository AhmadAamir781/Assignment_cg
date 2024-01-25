from django.urls import path
from .views import CreateUserView,RetrieveUserView,IngestStockDataView,RetrieveStockDataView,RetrieveSpecificStockDataView,PostTransactionView,RetrieveUserTransactionsView,RetrieveUserTransactionsByTimestampView
urlpatterns = [
    path('user/', CreateUserView.as_view(), name="create_user"),
    path('user/<str:username>/', RetrieveUserView.as_view(), name="rUser"),
    path('ingestStok/', IngestStockDataView.as_view(), name="ingest"),
    path('rStock/', RetrieveStockDataView.as_view(), name="rStock"),
    path('rspecificStock/', RetrieveSpecificStockDataView.as_view(), name="rSStock"),
    path('postTransaction/', PostTransactionView.as_view(), name="postTrans"),
    path('rUserTransaction/', RetrieveUserTransactionsView.as_view(), name="rUser"),
    path('rUserTransactionbytime/', RetrieveUserTransactionsByTimestampView.as_view(), name="rUsertransbytime"),
]
