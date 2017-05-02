from django.conf.urls import url
from django_filters.views import FilterView

from accounting import views
from accounting.filters import TransactionFilter
from accounting.models import Transaction

app_name = 'accounting'

urlpatterns = [
    url(r'^$', FilterView.as_view(model=Transaction, filterset_class=TransactionFilter), name='transaction_list'),
    url(r'^new_transaction/$', views.TransactionCreateView.as_view(), name='new_transaction'),
    url(r'^transaction/(?P<pk>\d+)/edit/$', views.TransactionUpdateView.as_view(), name='transaction_edit'),
    url(r'^transaction/(?P<pk>\d+)/delete/$', views.TransactionDeleteView.as_view(), name='transaction_delete'),
]
