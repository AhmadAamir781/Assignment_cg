from django.db import models

# Create your models here.
class CustomUser(models.Model):
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    balance = models.DecimalField(default=0, blank=True, max_digits=10, decimal_places=2)
    
class StockData(models.Model):
    ticker = models.CharField(max_length=10)
    open_price = models.DecimalField(max_digits=10 , decimal_places=2)
    close_price = models.DecimalField(max_digits=10 , decimal_places=2)
    high = models.DecimalField(max_digits=10 , decimal_places=2)
    low = models.DecimalField(max_digits=10 , decimal_places=2)
    Volume = models.DecimalField(max_digits=10 , decimal_places=2)
    timestamp = models.DateField(auto_now_add=True)

class Transactions(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, default=None, blank=True, null=True)
    ticker = models.CharField(max_length=155, default=None, blank=True, null=True)
    transaction_type = models.CharField(max_length = 4, choices =[('buy' , 'Buy'),('sell','Sell')])
    transaction_volume = models.DecimalField(max_digits = 10 , decimal_places = 2, default=0)
    transaction_price = models.DecimalField(max_digits = 10 , decimal_places = 2, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)