from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import StockData

class StockDataAPITests(APITestCase):
    def setUp(self):
        # Setup run before every test method.
        self.client = APIClient()
        self.stock_data = StockData.objects.create(
            ticker='AAPL',
            open_price=150.00,
            close_price=155.00,
            high=160.00,
            low=149.00,
            volume=100
        )
        self.stock_url = reverse('stock')
        self.specific_stock_url = reverse('stocks-ticker', kwargs={'ticker': 'AAPL'})
        self.stock_payload = {
            'ticker': 'GOOG',
            'open_price': 1520.00,
            'close_price': 1525.00,
            'high': 1530.00,
            'low': 1510.00,
            'volume': 300
        }

    def test_get_all_stock_data(self):
        response = self.client.get(self.stock_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 

    def test_ingest_stock_data_success(self):
        response = self.client.post(self.stock_url, self.stock_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "Stock data ingested successfully.")

    def test_ingest_stock_data_failure(self):
        invalid_payload = self.stock_payload.copy()
        del invalid_payload['ticker']
        response = self.client.post(self.stock_url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_specific_stock_data(self):
        response = self.client.get(self.specific_stock_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['ticker'], 'AAPL')

    def test_get_specific_stock_data_not_found(self):
        url = reverse('stocks-ticker', kwargs={'ticker': 'NONEXISTENT'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0) 

