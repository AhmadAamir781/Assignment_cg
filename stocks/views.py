from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status   
from .serializers import StockDataSerializer
from .models import StockData

class RetrieveStockDataView(APIView):
    def get(self, request):
        stock_data = StockData.objects.all()
        serializer = StockDataSerializer(stock_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StockDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Stock data ingested successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveSpecificStockDataView(APIView):
    def get(self, request, ticker):
        stock_data = StockData.objects.filter(ticker=ticker)
        serializer = StockDataSerializer(stock_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

