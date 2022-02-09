from django_filters import rest_framework as filters
from inventory_manage.models import Purchase, Sale, Inventory, Customer, Vendor


class PurchaseFilter(filters.FilterSet):


    class Meta:
        model = Purchase
        fields = ['po_no', "item", "vendor"]