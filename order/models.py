import datetime
import arrow
from django.utils.translation import ugettext_lazy as _
from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from ims_auth.models import User
from products.models import Item
from clients.models import Customer, Vendor
from order.utils import ORDER_STATUS, CURRENCY_CODES




# Purchase Order Model
class PurchaseOrder(models.Model):
    purchase_title = models.CharField("Purchase Title", max_length=50, blank=True, null=True)
    prefix = models.CharField(max_length=20, default='PO-')
    po_no = models.CharField("Purchase Number", editable=False, max_length=50, unique=True, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.DO_NOTHING)
    # items = models.ManyToManyField('PurchaseItem')
    orderstatus = models.CharField('OrderStatus', max_length=100, choices=ORDER_STATUS)
    created_date = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(User, related_name="purchase_created_by", on_delete=models.CASCADE, null=True)

    class Meta:
        """Meta definition for Purchase Order."""

        verbose_name = "Purchase Order"
        verbose_name_plural = "Purchase Orders"

    def __str__(self):
        """Unicode representation of Purchase Order."""
        return f'{self.prefix}{self.po_no}'

    def save(self, *args, **kwargs):
        if not self.po_no:
            self.po_no = self.po_id_generator()
            while PurchaseOrder.objects.filter(po_no=self.po_no).exists():
                self.po_no = self.po_id_generator(
                    prev_po_no=self.po_no
                )
        super(PurchaseOrder, self).save(*args, **kwargs)

    def po_id_generator(self, prev_po_no=None):
        if prev_po_no:
            prev_po_no += 1
            return prev_po_no
        date = datetime.datetime.now().strftime("%Y")
        return int(date + "0001")




class PurchaseItem(models.Model):
    po = models.ForeignKey(PurchaseOrder, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField("Quantity", default=0)
    status = models.CharField('Item status', max_length=30,  blank=False, null=False)
    price = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CODES, blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True, null=True)


    class Meta:
        """Meta definition for Purchase Order."""

        verbose_name = "Purchase Item"
        verbose_name_plural = "Add Purchase Item"




# Purchase Billing Model.
class PurchaseBilling(models.Model):
    po_no = models.ForeignKey(PurchaseOrder, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(PurchaseItem, on_delete=models.DO_NOTHING)
    vendor = models.ForeignKey(Vendor, on_delete=models.DO_NOTHING)
    # sub_total is item of price and quantity
    sub_total = models.DecimalField(blank=True, null=True, max_digits=12, decimal_places=2)
    tax = models.DecimalField(blank=True, null=True, max_digits=12, decimal_places=2)
    shipping_price = models.DecimalField(blank=True, null=True, max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CODES, blank=True, null=True)
    other_amt = models.DecimalField(blank=True, null=True, max_digits=12, decimal_places=2)
    status = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        "Meta definition for Purchase Billing."

        verbose_name = "Purchase Bill"
        verbose_plural_name = "Purchased Bill"

    def __str__(self):
        return self.so_no

    def formatted_sub_total(self):
        return self.currency + " " + str(self.sub_total)

    def formatted_other_amt(self):
        return str(self.other_amt) + " " + self.currency

    def formatted_shipping_price(self):
        return str(self.shipping_price) + " " + self.currency



# Paid Purchase Bill Model.
class PaidPurchaseBill(models.Model):
    PB_no = models.ForeignKey(
        PurchaseBilling, related_name='Purchased Bill', on_delete=models.DO_NOTHING, blank=True, null=True
    )
    amount_due = models.DecimalField(blank=True, null=True, max_digits=12, decimal_places=2)
    amount_paid = models.DecimalField(blank=True, null=True, max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CODES, blank=True, null=True)
    status = models.CharField(max_length=15, choices=ORDER_STATUS, default="Draft")
    details = models.TextField("Details", null=True, blank=True)
    due_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="paid_purchase_created_by", on_delete=models.SET_NULL, null=True
    )
    is_email_sent = models.BooleanField(default=False)

    # teams = models.ForeignKey()
    class Meta:
        "Meta definition for Purchased Bill."

        verbose_name = "Paid Purchased Bill"
        verbose_plural_name = "Paid Purchased Bill"

    def __str__(self):
        return self.PB_no

    def formatted_amount_paid(self):
        return self.currency + " " + str(self.amount_paid)

    def formatted_amount_due(self):
        return self.currency + " " + str(self.amount_due)

    def is_draft(self):
        if self.status == "Draft":
            return True
        else:
            return False

    def is_sent(self):
        if self.status == "Sent" and self.is_email_sent == False:
            return True
        else:
            return False

    def is_resent(self):
        if self.status == "Sent" and self.is_email_sent == True:
            return True
        else:
            return False

    def is_paid_or_cancelled(self):
        if self.status in ["Paid", "Cancelled"]:
            return True
        else:
            return False

    def is_partly_paid(self):
        return self.amount_paid > 0

    @property
    def created_date_arrow(self):
        return arrow.get(self.created_date).humanize()



# sale Order Model
class SaleOrder(models.Model):
    purchase_title = models.CharField("Sale Title", max_length=50, blank=True, null=True)
    prefix = models.CharField(max_length=20, default='SO-')
    so_no = models.CharField("Sales Number", editable=False, max_length=50, unique=True, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, null=True)
    # items = models.ManyToManyField('SalesItem')
    orderstatus = models.CharField('Order Status', max_length=100, choices=ORDER_STATUS)
    created_date = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(User, related_name="sale_created_by", on_delete=models.CASCADE, null=True)

    class Meta:
        """Meta definition for SAle Order."""

        verbose_name = "Sale Order"
        verbose_name_plural = "Sale Orders"

    def __str__(self):
        """Unicode representation of Sale Order."""
        return f'{self.prefix}{self.so_no}'

    def save(self, *args, **kwargs):
        if not self.so_no:
            self.so_no = self.so_id_generator()
            while SaleOrder.objects.filter(so_no=self.so_no).exists():
                self.so_no = self.so_id_generator(
                    prev_so_no=self.so_no
                )
        super(SaleOrder, self).save(*args, **kwargs)

    def so_id_generator(self, prev_so_no=None):
        if prev_so_no:
            prev_so_no += 1
            return prev_so_no
        date = datetime.datetime.now().strftime("%Y")
        return int(date + "0001")



# sale Item Line Model.
class SalesItem(models.Model):
    so = models.ForeignKey(SaleOrder, on_delete=models.DO_NOTHING, blank=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField("Quantity", default=0)
    status = models.CharField('Item status', max_length=30,  blank=False, null=False)
    price = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CODES, blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True, null=True)


    class Meta:
        """Meta definition for Purchase Order."""

        verbose_name = "Sale Item"
        verbose_name_plural = "Add Sale Item"

    def __str__(self):
        return self.so

    def formatted_price(self):
        return str(self.price) + " " + self.currency

    def formatted_quantity(self):
        return str(self.quantity) + " " + "qty"


"""
# Sales Billing Model
class SalesBilling(models.Model):
    so_no = models.ForeignKey(SaleOrder, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(SalesItem, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    # sub_total is item of price and quantity
    sub_total = models.DecimalField(blank=True, null=True, max_digits=12, decimal_places=2)
    tax = models.DecimalField(blank=True, null=True, max_digits=12, decimal_places=2)
    shipping_price = models.DecimalField(blank=True, null=True, max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CODES, blank=True, null=True)
    other_amt = models.DecimalField("Other Amount", blank=True, null=True, max_digits=12, decimal_places=2)
    status = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True, null=True)
    
    
    class Meta:
        "Meta definition for Sales Billing."
        
        verbose_name = "Sales Billing"
        verbose_plural_name = "Sale Billing"
    
    def __str__(self):
        return self.so_no
    
    
    def formatted_sub_total(self):
        return self.currency + " " + str(self.sub_total)
    
    def formatted_other_amt(self):
        return str(self.other_amt) + " " + self.currency
    
    def formatted_shipping_price(self):
        return str(self.shipping_price) + " " + self.currency
    
    

# Paid Sales Bill Model.
class PaidSalesBill(models.Model):
    SB_no = models.ForeignKey(
        SalesBilling, related_name='Saled Bill', on_delete=models.DO_NOTHING, blank=True, null=True
    )
    amount_due =models.DecimalField(blank=True, null=True, max_digits=12, decimal_places=2)
    amount_paid = models.DecimalField(blank=True, null=True, max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CODES, blank=True, null=True)
    status = models.CharField(max_length=15, choices=ORDER_STATUS, default="Draft")
    details = models.TextField("Details", null=True, blank=True)
    due_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="paid_sale_created_by", on_delete=models.SET_NULL, null=True
    )
    is_email_sent = models.BooleanField(default=False)
    # teams = models.ForeignKey()
    class Meta:
        "Meta definition for Saled Bill."
        
        verbose_name = "Paid Sales Bill"
        verbose_plural_name = "Paid Sale Bill"
    
    def __str__(self):
        return self.SB_no
    
    def formatted_amount_paid(self):
        return self.currency + " " + str(self.amount_paid)
    
    def formatted_amount_due(self):
        return self.currency + " " + str(self.amount_due)
    
    def is_draft(self):
        if self.status == "Draft":
            return True
        else:
            return False
    
    def is_sent(self):
        if self.status == "Sent" and self.is_email_sent == False:
            return True
        else:
            return False
    
    def is_resent(self):
        if self.status == "Sent" and self.is_email_sent == True:
            return True
        else:
            return False
        
    def is_paid_or_cancelled(self):
        if self.status in ["Paid", "Cancelled"]:
            return True
        else:
            return False
    
    @property
    def created_date_arrow(self):
        return arrow.get(self.created_date).humanize()
 """
