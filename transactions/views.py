from datetime import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import CustomUser
from .models import Transactions
from .serializers import TransactionsSerializer

class PostTransactionView(APIView):
    """
    API view for posting transactions and retrieving user transactions.
    """
    def post(self, request):
        # Validate and save transaction data
        serializer = TransactionsSerializer(data=request.data)
        if serializer.is_valid():
            # Calculate transaction_price based on the assumed stock price
            stock_price = 10.0  # Replace with actual stock price retrieval logic
            transaction_volume = serializer.validated_data['transaction_volume']
            serializer.validated_data['transaction_price'] = stock_price * transaction_volume

            # Save transaction data
            serializer.save()

            # Update user balance
            user_id = serializer.validated_data['user'].id
            user = CustomUser.objects.get(id=user_id)
            user.balance -= serializer.validated_data['transaction_price']
            user.save()

            return Response({"message": "Transaction posted successfully."}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, user_id):
        # Retrieve user transactions
        transactions = Transactions.objects.filter(user__id=user_id)
        serializer = TransactionsSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RetrieveUserTransactionsByTimestampView(APIView):
    """
    API view for retrieving user transactions within a specified timestamp range.
    """
    def get(self, request, user_id, start_timestamp, end_timestamp):
        try:
            start_datetime = datetime.fromisoformat(start_timestamp)
            end_datetime = datetime.fromisoformat(end_timestamp)
        except ValueError:
            return Response({'detail': 'Invalid timestamp format'}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve user transactions within the specified timestamp range
        transactions = Transactions.objects.filter(
            user__id=user_id,
            timestamp__gte=start_datetime,
            timestamp__lte=end_datetime
        )
        serializer = TransactionsSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
