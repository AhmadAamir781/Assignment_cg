from django.urls import path
from .views import RetrieveStockDataView,RetrieveSpecificStockDataView
urlpatterns = [
    path('stocks/', RetrieveStockDataView.as_view(), name="stock"),
    path('stocks/<str:ticker>/', RetrieveSpecificStockDataView.as_view(), name="stocks-ticker")
]
