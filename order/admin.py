from django.contrib import admin
from order.models import PurchaseOrder, PurchaseItem, SaleOrder, SalesItem


# Register your models here.
admin.site.register(PurchaseOrder)
admin.site.register(PurchaseItem)
admin.site.register(SaleOrder)
admin.site.register(SalesItem)
