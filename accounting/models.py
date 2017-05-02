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
    BANKLINE = 'bl'
    CASH = 'c'
    CREDIT_CARD = 'cc'
    DEBIT_CARD = 'dc'
    PAYMENT_TYPES = (
        (BANKLINE,'Bankline'),
        (CASH,'Cash'),
        (CREDIT_CARD,'Credit Card'),
        (DEBIT_CARD,'Debit Card')
    )
    paymentType = models.CharField(max_length=2,
                                       choices=PAYMENT_TYPES,
                                       default=CREDIT_CARD)
    date = models.DateField(default=timezone.now)
    amount = models.DecimalField(max_digits=7,decimal_places=2,null=False,blank=False)
    location = models.CharField(max_length=100)
    notes = models.CharField(max_length=255)
    transactionType = models.CharField(max_length=1,
                                       choices=TRANSACTION_TYPES,
                                       default=EXPENSE)
    author = models.ForeignKey('auth.User',default=1)
    category = models.ForeignKey('accounting.TransactionCategory',related_name='transactions',null=False,blank=False)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.notes

    def get_absolute_url(self):
        return reverse('accounting:transaction_list')

class TransactionCategory(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    author = models.ForeignKey('auth.User',default=1)

    def __str__(self):
        return self.name