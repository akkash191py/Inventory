from django_filters import rest_framework as filters
from products.models import Item, ProductCategory


class ItemFilter(filters.FilterSet):
    # min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    # max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Item
        fields = ['sku', 'barcode', 'name', 'category__name', 'brand__name']
        # fields = ['category', 'brand', 'min_price', 'max_price']