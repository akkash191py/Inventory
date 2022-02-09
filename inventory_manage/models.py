from django.db import models
from products.models import Item
from clients.models import Customer, Vendor
# from stock_mg.models import StockReceive, StockIssue,StockRecord
from ims_auth.models import User


PAYMENT_STATUS = (
    ("Pending", "Pending"),
    ("Completed", "Completed"),
    ("Processing", "Processing"),
    ("Cancelled", "Cancelled"),
)

# Purchase Order Model
class Purchase(models.Model):
    po_no = models.CharField("PO no", max_length=13, unique=True, help_text="Enter Purchase Order Number")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default='0', blank=True, null=True)
    price = models.FloatField(default='0', blank=True, null=True)
    total_amt = models.FloatField("Total amount", editable=False, null=True)
    # remaining_amt = models.FloatField("Remaining amount", editable=False, null=True)
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS)
    pur_date = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name_plural = '1. Purchase Order'

    def __str__(self):
        return self.po_no

    def save(self, *args, **kwargs):
        self.total_amt = self.quantity * self.price
        super(Purchase, self).save(*args, **kwargs)

        # Inventory effect
        inventory = Inventory.objects.filter(item = self.item).order_by('-id').first()
        if inventory:
            totalBal = inventory.total_bal_qty + self.quantity
        else:
            totalBal = self.quantity

        Inventory.objects.create(
            item = self.item,
            purchase = self,
            sale = None,
            pur_qty = self.quantity,
            sale_qty =None,
            total_bal_qty =totalBal
        )


# Sale Model
class Sale(models.Model):
    sale_no = models.CharField("Sale no", max_length=13, unique=True, help_text="Enter Sale Order Number")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default='0', blank=True, null=True)
    price = models.FloatField(default='0', blank=True, null=True)
    total_amt = models.FloatField("Total amount", editable=False, null=True)
    # remaining_amt = models.FloatField("Remaining amount", editable=False, null=True)
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS)
    sale_date = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name_plural = '2. Sale'

    def __str__(self):
        return self.sale_no

    def save(self, *args, **kwargs):
        self.total_amt = self.quantity * self.price
        super(Sale, self).save(*args, **kwargs)

        # Inventory effect
        inventory = Inventory.objects.filter(item = self.item).order_by('-id').first()
        if inventory:
            totalBal = inventory.total_bal_qty - self.quantity
        else:
            totalBal = self.quantity

        Inventory.objects.create(
            item = self.item,
            purchase = None,
            sale = self,
            pur_qty = None,
            sale_qty =self.quantity,
            total_bal_qty =totalBal
        )




# Inventory Model
class Inventory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, default=0,
                                      null=True)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, default=0,
                                    null=True)
    pur_qty = models.PositiveIntegerField(default=0, editable=False, null=True)
    sale_qty = models.PositiveIntegerField(default=0, editable=False, null=True)
    total_bal_qty = models.PositiveIntegerField(editable=False)

    class Meta:
        verbose_name_plural = "3. Inventory"

    def purchase_dte(self):
        if self.purchase:
            return self.purchase.pur_date

    def sale_dte(self):
        if self.sale:
            return self.sale.sale_date
