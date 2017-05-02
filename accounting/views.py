from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from accounting.forms import TransactionForm
from accounting.models import Transaction, TransactionCategory


class TransactionCreateView(CreateView):
    form_class = TransactionForm
    model = Transaction

class TransactionUpdateView(UpdateView):
    form_class = TransactionForm
    model = Transaction

class TransactionDeleteView(DeleteView):
    model = Transaction
    success_url = reverse_lazy('accounting:transaction_list')

class TransactionListView(ListView):
    model = Transaction

    def get_queryset(self):
        return Transaction.objects.order_by('date')

    def get_context_data(self, **kwargs):
        context = super(TransactionListView, self).get_context_data(**kwargs)
        context['transaction_total_amount'] = sum(t.amount for t in self.object_list)
        return context