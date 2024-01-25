from .models import StockData
from rest_framework import serializers
class StockDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockData
        fields = '__all__'