from django.contrib import admin
from .models import CustomUser,Transactions,StockData
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Transactions)
admin.site.register(StockData)
