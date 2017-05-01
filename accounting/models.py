from django.db import models

# Create your models here.
from django.utils import timezone


class Transaction(models.Model):
    EXPENSE = 'e'
    INCOME = 'i'
    REFUND = 'r'
    TRANSACTION_TYPES = (
        (EXPENSE,'Expense'),
        (INCOME,'Income'),
        (REFUND,'Refund')
    )
    date = models.DateField(default=timezone.now)
    amount = models.DecimalField(max_digits=5,decimal_places=2,null=False,blank=False)
    notes = models.CharField(max_length=255)
    transactionType = models.CharField(max_length=1,
                                       choices=TRANSACTION_TYPES,
                                       default=EXPENSE)
    category = models.ForeignKey('accounting.TransactionCategory',related_name='transactions',null=False,blank=False)

class TransactionCategory(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)