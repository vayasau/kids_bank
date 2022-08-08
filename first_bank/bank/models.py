from django.db import models
from datetime import date

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=31)

    def __str__(self):
        return self.name


class Money(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    trans_date = models.DateField('transaction date', default=date.today)
    interest_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.balance


class Interest(models.Model):
    interest_rate = models.DecimalField(max_digits=3, decimal_places=1, default=0)

    def __str__(self):
        return self.interest