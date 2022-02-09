from django.contrib import admin
from inventory_manage.models import Purchase, Sale, Inventory
from import_export.admin import ImportExportModelAdmin


# Purchase Admin Model
class PurchaseAdmin(ImportExportModelAdmin):
    list_display = ["id", "po_no", "item", "vendor", "quantity", "price",
                    "total_amt", "payment_status", "pur_date"]

    list_filter = ["id", "po_no", "item", "vendor"]
    search_fields = ["po_no", "item", "vendor"]
admin.site.register(Purchase, PurchaseAdmin)


# sale Admin Model
class SaleAdmin(ImportExportModelAdmin):
    list_display = ["id", "sale_no", "item", "customer", "quantity", "price",
                    "total_amt", "payment_status", "sale_date"]

    list_filter = ["id", "sale_no", "item", "customer"]
    search_fields = ["sale_no", "item", "customer"]
admin.site.register(Sale, SaleAdmin)

# Inventory Admin Model
class InventoryAdmin(ImportExportModelAdmin):
    list_display = ["id", "item", "purchase", "sale", "pur_qty", "sale_qty", "total_bal_qty", "purchase_dte", "sale_dte"]
    list_filter = ["item","purchase", "sale"]
    search_fields = ["item", "purchase", "sale"]
admin.site.register(Inventory, InventoryAdmin)