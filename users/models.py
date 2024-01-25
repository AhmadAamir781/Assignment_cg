from django.db import models

# Create your models here.
class CustomUser(models.Model):
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    balance = models.DecimalField(default=0, blank=True, max_digits=10, decimal_places=2)