from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transactions
from .serializers import TransactionsSerializer
from users.models import CustomUser
from stocks.models import StockData  

class TransactionView(APIView):
    """
    API view for posting transactions and retrieving user transactions.
    """
    def post(self, request):

        # Create a new transaction serializer instance with the provided data
        serializer = TransactionsSerializer(data=request.data)

        # Validate the serializer data
        if serializer.is_valid():
            serializer.save()
            
            return Response({"message": "Transaction posted successfully."}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, user_id):
        # Retrieve user transactions
        user = CustomUser.objects.filter(id=user_id).first()
        transactions = Transactions.objects.filter(user=user)
        print(transactions)
        return Response({"Transactions": transactions}, status=status.HTTP_200_OK)

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
            user_id=user_id,
            timestamp__gte=start_datetime,
            timestamp__lte=end_datetime
        )
        serializer = TransactionsSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
