from django.conf.urls import url

from accounting import views

urlpatterns = [
    url(r'^$', views.TransactionCreateView.as_view(),name='new_transaction'),
]