from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from accounting.forms import TransactionForm
from accounting.models import Transaction


class TransactionCreateView(CreateView):
    template_name = 'accounting/new_transaction.html'
    form_class = TransactionForm
    model = Transaction