from django_filters import rest_framework as filters
from stock_mg.models import StockReceive, StockIssue, totalinstock, totaloutstock


class StockReceiveFilter(filters.FilterSet):


    class Meta:
        model = StockReceive
        fields = ['items', 'batch_no']

class StockIssueFilter(filters.FilterSet):


    class Meta:
        model = StockIssue
        fields = ['items', 'issue_no']

class totalinstockFilter(filters.FilterSet):


    class Meta:
        model = totalinstock
        fields = ['item']

class totaloutstockFilter(filters.FilterSet):


    class Meta:
        model = totaloutstock
        fields = ['item']
