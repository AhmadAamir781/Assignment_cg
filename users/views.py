# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser, StockData, Transactions
from .serializers import UserSerializer, StockDataSerializer, TransactionsSerializer
from datetime import datetime

class CreateUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveUserView(APIView):
    def get(self, request, username):
        user = CustomUser.objects.filter(username=username).first()
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

class IngestStockDataView(APIView):
    def post(self, request):
        serializer = StockDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Stock data ingested successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveStockDataView(APIView):
    def get(self, request):
        stock_data = StockData.objects.all()
        serializer = StockDataSerializer(stock_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RetrieveSpecificStockDataView(APIView):
    def get(self, request, ticker):
        stock_data = StockData.objects.filter(ticker=ticker)
        serializer = StockDataSerializer(stock_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PostTransactionView(APIView):
    def post(self, request):
        serializer = TransactionsSerializer(data=request.data)
        if serializer.is_valid():
            # Calculate transaction_price based on the current stock price (assumption)
            stock_price = 10.0  # Replace with actual stock price retrieval logic
            transaction_volume = serializer.validated_data['transaction_volume']
            serializer.validated_data['transaction_price'] = stock_price * transaction_volume

            serializer.save()

            # Update user's balance
            user_id = serializer.validated_data['user'].id
            user = CustomUser.objects.get(id=user_id)
            user.balance -= serializer.validated_data['transaction_price']
            user.save()

            return Response({"message": "Transaction posted successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveUserTransactionsView(APIView):
    def get(self, request, user_id):
        transactions = Transactions.objects.filter(user__id=user_id)
        serializer = TransactionsSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RetrieveUserTransactionsByTimestampView(APIView):
    def get(self, request, user_id, start_timestamp, end_timestamp):
        start_datetime = datetime.fromisoformat(start_timestamp)
        end_datetime = datetime.fromisoformat(end_timestamp)

        transactions = Transactions.objects.filter(
            user__id=user_id,
            timestamp__gte=start_datetime,
            timestamp__lte=end_datetime
        )
        serializer = TransactionsSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
