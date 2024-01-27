from django.urls import path
from .views import StockDataView,RetrieveSpecificStockDataView
urlpatterns = [
    path('stocks/', StockDataView.as_view(), name="stock"),
    path('stocks/<str:ticker>/', RetrieveSpecificStockDataView.as_view(), name="stocks-ticker")
]
