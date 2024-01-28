from django.db import models

class StockData(models.Model):
    ticker = models.CharField(unique = True,  max_length=10,null=True )
    open_price = models.DecimalField(max_digits=10 , decimal_places=2)
    close_price = models.DecimalField(max_digits=10 , decimal_places=2)
    high = models.DecimalField(max_digits=10 , decimal_places=2)
    low = models.DecimalField(max_digits=10 , decimal_places=2)
    volume = models.DecimalField(max_digits=10 , decimal_places=2)
    timestamp = models.DateField(auto_now_add=True)