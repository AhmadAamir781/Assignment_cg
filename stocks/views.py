from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import StockDataSerializer
from .models import StockData

class StockDataView(APIView):
    """
    API view for retrieving and ingesting stock data.
    """
    def get(self, request):
        """
        Retrieve all stock data entries.
        """
        stock_data = StockData.objects.all()
        serializer = StockDataSerializer(stock_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Ingest new stock data.
        """
        serializer = StockDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Stock data ingested successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveSpecificStockDataView(APIView):
    """
    API view for retrieving specific stock data based on ticker.
    """
    def get(self, request, ticker):
        """
        Retrieve stock data for a specific ticker.
        """
        stock_data = StockData.objects.filter(ticker=ticker)
        serializer = StockDataSerializer(stock_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
