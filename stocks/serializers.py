from .models import StockData
from rest_framework import serializers
class StockDataSerializer(serializers.ModelSerializer):
    ticker = serializers.CharField(max_length=10)
    open_price = serializers.DecimalField(max_digits=10 , decimal_places=2,required = True)
    close_price = serializers.DecimalField(max_digits=10 , decimal_places=2,required = True)
    high = serializers.DecimalField(max_digits=10 , decimal_places=2,required = True)
    low = serializers.DecimalField(max_digits=10 , decimal_places=2,required = True)
    volume = serializers.DecimalField(max_digits=10 , decimal_places=2,required = True)
    class Meta:
        model = StockData
        fields = '__all__'