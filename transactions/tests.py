from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import CustomUser, StockData, Transactions

class TransactionsAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create(username='testuser', balance=1000.00)
        self.stock_data = StockData.objects.create(ticker='AAPL', open_price=150.00, close_price=155.00, high=160.00, low=149.00, volume=100)
        self.transaction_url = reverse('transactions')
        self.transaction_data = {
            'user_id': self.user.id,
            'ticker': self.stock_data.ticker,
            'transaction_type': 'buy',
            'transaction_volume': 5
        }

    def test_create_transaction_success(self):
        response = self.client.post(self.transaction_url, self.transaction_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "Transaction posted successfully.")

    def test_create_transaction_insufficient_balance(self):
        self.transaction_data['transaction_volume'] = 100 
        response = self.client.post(self.transaction_url, self.transaction_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_user_transactions(self):
        Transactions.objects.create(user=self.user, ticker=self.stock_data, transaction_type='buy', transaction_volume=5, transaction_price=750.00)
        response = self.client.get(reverse('transactionsUser', kwargs={'user_id': self.user.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 
    def test_get_user_transactions_by_timestamp(self):
        transaction = Transactions.objects.create(user=self.user, ticker=self.stock_data, transaction_type='buy', transaction_volume=5, transaction_price=750.00)
        start_timestamp = transaction.timestamp.isoformat()
        end_timestamp = transaction.timestamp.isoformat()
        url = reverse('rUsertransbytime', kwargs={
            'user_id': self.user.id,
            'start_timestamp': start_timestamp,
            'end_timestamp': end_timestamp
        })
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

