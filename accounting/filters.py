import datetime

import django_filters

from accounting.models import Transaction


class TransactionFilter(django_filters.FilterSet):
    date__year = django_filters.NumberFilter(name='date', lookup_expr='year__exact')

    def __init__(self, *args, **kwargs):
        super(TransactionFilter,self).__init__(*args, **kwargs)
        now = datetime.datetime.now();
        self.form.initial['date__year'] = now.year
        self.form.initial['date__month'] = now.month



    class Meta:
        model = Transaction
        fields = {'date':['year__exact','month__exact'],'notes':['icontains'],'category':['exact'],'transactionType':['exact']
            , 'paymentType': ['exact']}

