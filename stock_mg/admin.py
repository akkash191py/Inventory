from django.contrib import admin
from stock_mg.models import StockReceive, StockIssue, totalinstock, totaloutstock
from import_export.admin import ImportExportModelAdmin


# Stock Receive ImportExport Model Admin
"""class StockAdmin(ImportExportModelAdmin):
    list_display = ['id', 'category', 'items', 'quantity', 'receive_quantity', 'issue_quantity', 'issue_by', 'issue_to', 'receive_by', 'reorder_level', 'last_updated']
    serializer_class = StockSerializer
    list_filter = ['category', 'items', 'quantity', 'receive_quantity', 'receive_by']
    search_fields = ['category__name', 'items__name']

admin.site.register(Stock, StockAdmin)
"""

# Stock Receive ImportExport Model Admin
class StockReceiveAdmin(ImportExportModelAdmin):
    list_display = ["id", "batch_no", "items", "receive_qty", "receive_by", "receive_dte"]
    list_filter = ["batch_no", "items", "receive_qty", "receive_by", "receive_dte"]
    search_fields = ['items__name']
admin.site.register(StockReceive, StockReceiveAdmin)

# Stock Issue ImportExport Model Admin
class StockIssueAdmin(ImportExportModelAdmin):
    list_display = ["id", "issue_no", "items", "issue_qty", "issue_by", "issue_dte"]
    list_filter = ["issue_no", "items", "issue_qty", "issue_by", "issue_dte"]
    search_fields = ['items__name']
admin.site.register(StockIssue, StockIssueAdmin)

# Stock Record ImportExport Model Admin
"""class StockRecordAdmin(ImportExportModelAdmin):
    list_display = ["id","item", "stock_receive", "stock_issue", "total_receive_qty",
                    "total_issue_qty", "total_bal_qty", "receive_date", "issue_date"]
    list_filter = ["item", "stock_receive", "stock_issue", "total_receive_qty", "total_issue_qty", "total_bal_qty"]
    search_fields = ['items__name']
admin.site.register(StockRecord, StockRecordAdmin)"""


class totalinstockAdmin(admin.ModelAdmin):
    list_display = ["id", "item", "total_receive_qty"]
    # list_filter = ["stockin__item"]
    # search_fields = ['item']
admin.site.register(totalinstock, totalinstockAdmin)


class totaloutstockAdmin(admin.ModelAdmin):
    list_display = ["id", "item", "total_issue_qty"]
    # list_filter = ["stockin__item"]
    # search_fields = ['item']
admin.site.register(totaloutstock, totaloutstockAdmin)
