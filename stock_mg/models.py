from django.db import models
from products.models import Item
# from django.db.models.signals import pre_save,post_save
# from django.dispatch import receiver
from ims_auth.models import User


class totalinstock(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)

    # stockin = models.ForeignKey(StockIn, on_delete=models.CASCADE, blank=True, null=True)

    @property
    def total_receive_qty(self):
        receive_items = StockReceive.objects.filter(stock_id=self.id)
        total_qty = 0
        for receive_item in receive_items:
            total_qty = (receive_item.receive_qty + total_qty)
        return total_qty

    def __str__(self):
        return self.item.name

    class Meta:
        # ordering = ("-receive_dte")
        verbose_name_plural = " 3. Total Received"


# Stock Receive Model
class StockReceive(models.Model):
    stock_id = models.ForeignKey(totalinstock, on_delete=models.CASCADE, blank=True, null=True)
    items = models.ForeignKey(Item, related_name="Item_name", on_delete=models.CASCADE, blank=True, null=True)
    batch_no = models.CharField("Batch no", unique=True, max_length=30, blank=True, null=True)
    receive_qty = models.IntegerField(blank=True, null=True)
    receive_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    receive_dte = models.DateTimeField("Receive date", auto_now_add=False, auto_now=True)

    class Meta:
        # ordering = ("-receive_dte")
        verbose_name_plural = "1. Stock Receive"

    def __str__(self):
        return str(self.batch_no)





class totaloutstock(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)

    # stockin = models.ForeignKey(StockIn, on_delete=models.CASCADE, blank=True, null=True)

    @property
    def total_issue_qty(self):
        issue_items = StockIssue.objects.filter(stock_id=self.id)
        total_qty = 0
        for issue_item in issue_items:
            total_qty = (issue_item.issue_qty + total_qty)
        return total_qty

    def __str__(self):
        return self.item.name

    class Meta:
        # ordering = ("-issue_dte")
        verbose_name_plural = "4. Total Issued"



# Stock Issue Model
class StockIssue(models.Model):
    stock_id = models.ForeignKey(totaloutstock, on_delete=models.CASCADE, blank=True, null=True)
    items = models.ForeignKey(Item, related_name="Itemname", on_delete=models.CASCADE, blank=True, null=True)
    issue_no = models.CharField("Issue no", max_length=30, unique=True, blank=True, null=True)
    issue_qty = models.IntegerField(default='0', blank=True, null=True)
    issue_dte = models.DateTimeField("Issue date", auto_now_add=False, auto_now=True)
    issue_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        # ordering = ("-issue_dte")
        verbose_name_plural = "2. Stock Issue"

    def __str__(self):
        return str(self.issue_no)




# Stock Record Model
"""class StockRecord(models.Model):
    item = models.ForeignKey(Item, related_name="items", on_delete=models.CASCADE, blank=True, null=True)
    stock_receive = models.ForeignKey(StockReceive, related_name="stock_receive", on_delete=models.CASCADE, default=0, null=True)
    stock_issue = models.ForeignKey(StockIssue, related_name="stock_issue", on_delete=models.CASCADE, default=0, null=True)
    total_receive_qty = models.IntegerField(default=0, editable=False, null=True)
    total_issue_qty = models.IntegerField(default=0, editable=False, null=True)
    total_bal_qty = models.IntegerField(editable=False)

    class Meta:
        verbose_name_plural = "3. Stock Record"

    def receive_date(self):
        if self.stock_receive:
            return self.stock_receive.receive_dte

    def issue_date(self):
        if self.stock_issue:
            return self.stock_issue.issue_dte
"""





# Stock Record Model
"""class Stock(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    items = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    issue_quantity = models.IntegerField(default='0', blank=True, null=True)
    issue_by = models.CharField(max_length=50, blank=True, null=True)
    issue_to = models.CharField(max_length=50, blank=True, null=True)
    receive_by = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    class Meta:
        unique_together = [['category', 'items']]
        ordering = ('pk',)
"""


