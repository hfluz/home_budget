from django.db import models

# Create your models here.
from django.urls import reverse
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
    author = models.ForeignKey('auth.User',default=1)
    category = models.ForeignKey('accounting.TransactionCategory',related_name='transactions',null=False,blank=False)

    def __str__(self):
        return self.notes

    def get_absolute_url(self):
        return reverse('new_transaction')

class TransactionCategory(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    author = models.ForeignKey('auth.User',default=1)

    def __str__(self):
        return self.name