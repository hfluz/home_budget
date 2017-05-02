from django import forms

from accounting.models import Transaction


class TransactionForm(forms.ModelForm):

    class Meta():
        model = Transaction
        fields = ('date','transactionType','category','location','amount','notes')

        widgets = {
            'notes':forms.Textarea(attrs={'rows':3})
        }