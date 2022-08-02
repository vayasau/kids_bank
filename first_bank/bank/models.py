from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=31)
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)


class Money(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    transaction = models.CharField(max_length=7)
    trans_date = models.DateTimeField('transaction date', auto_now=True)