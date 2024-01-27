from django.db import models
from users.models import CustomUser
from stocks.models import StockData
class Transactions(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, default=None, blank=True, null=True)
    ticker = models.ForeignKey(StockData ,  on_delete = models.CASCADE, default=None, blank=True, null=True)
    transaction_type = models.CharField(max_length = 4, choices =[('buy' , 'Buy'),('sell','Sell')])
    transaction_volume = models.DecimalField(max_digits = 10 , decimal_places = 2, default=0)
    transaction_price = models.DecimalField(max_digits = 10 , decimal_places = 2, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
