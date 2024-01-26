from django.shortcuts import render
from rest_framework.views import APIView
from users.models import CustomUser
from .serializers import TransactionsSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Transactions
from datetime import datetime

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
        try:
            start_datetime = datetime.fromisoformat(start_timestamp)
            end_datetime = datetime.fromisoformat(end_timestamp)
        except ValueError:
            return Response({'detail': 'Invalid timestamp format'}, status=status.HTTP_400_BAD_REQUEST)

        transactions = Transactions.objects.filter(
            user__id=user_id,
            timestamp__gte=start_datetime,
            timestamp__lte=end_datetime
        )
        serializer = TransactionsSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
