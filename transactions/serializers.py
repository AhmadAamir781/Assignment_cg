from rest_framework import serializers
from .models import Transactions
from users.models import CustomUser
from stocks.models import StockData

class TransactionsSerializer(serializers.ModelSerializer):
    transaction_type = serializers.CharField(max_length=4, required=True)
    transaction_volume = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    user_id = serializers.IntegerField(required=True)
    ticker = serializers.CharField(required=True)

    class Meta:
        model = Transactions
        fields = '__all__'

    def validate_transaction_volume(self, value):
        if value < 0:
            raise serializers.ValidationError("Transaction volume must be a non-negative value.")
        return value

    def validate_transaction_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Transaction price must be a non-negative value.")
        return value
   
    def create(self, validated_data):
        # Extract user_id and ticker from the validated data
        user_id = validated_data.pop('user_id')
        ticker_symbol = validated_data.pop('ticker')

        # Retrieve the associated user and stock data
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("User not found.")

        try:
            stock_data = StockData.objects.get(ticker=ticker_symbol)
        except StockData.DoesNotExist:
            raise serializers.ValidationError("Stock not found.")

        # Calculate transaction_price based on the assumed stock price
        stock_price =   stock_data.low  # Replace with actual stock price retrieval logic
        transaction_price = float(stock_price) * float(validated_data['transaction_volume'])

        # Validate if the user has enough balance for the transaction
        if validated_data['transaction_type'] == 'buy' and user.balance < transaction_price:
            raise serializers.ValidationError("Insufficient balance for the transaction.")

        # Create and return the Transactions instance
        transaction = Transactions(
            user=user,
            ticker=stock_data,
            transaction_price=transaction_price,
            transaction_type=validated_data.get("transaction_type", None),
            transaction_volume=validated_data.get('transaction_volume',None)
        )

        # Update user balance based on transaction type
        if validated_data['transaction_type'] == 'buy':
            user.balance = float(user.balance) -  float(transaction_price)
        elif validated_data['transaction_type'] == 'sell':
            user.balance += float(user.balance) + float(transaction_price)
        user.save()

        return transaction