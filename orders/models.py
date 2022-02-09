import datetime
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from ims_auth.models import User
from products.models import Item
from clients.models import Customer, Vendor
from orders.utils import ORDER_STATUS, CURRENCY_CODES




# Purchase Order Model
"""class PurchaseOrder(models.Model):
    purchase_title = models.CharField("Purchase Title", max_length=50, blank=True, null=True)
    prefix = models.CharField(max_length=20, default='PO-')
    po_no = models.CharField("Purchase Number", editable=False, max_length=50, unique=True, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.DO_NOTHING)
    # items = models.ManyToManyField('PurchaseItem')
    orderstatus = models.CharField('OrderStatus', max_length=100, choices=ORDER_STATUS)
    created_date = models.DateTimeField(auto_now=True, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        Meta definition for Purchase Order.

        verbose_name = "Purchase Order"
        verbose_name_plural = "Purchase Orders"

    def __str__(self):
        Unicode representation of Purchase Order.
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
        return int(date + "0001")"""


"""@receiver(post_save, sender = PurchaseOrder)
def set_po_no(instance, created, **_kwargs):
    if created:
        instance.po_no = instance.product_prefix + "-" + str(0000+instance.id)"""


"""class PurchaseItem(models.Model):
    po = models.ForeignKey(PurchaseOrder, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField("Quantity")
    status = models.CharField('Item status', max_length=30,  blank=False, null=False)
    created_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        Meta definition for Purchase Order.

        verbose_name = "Purchase Item"
        verbose_name_plural = "Add Purchase Item" """


"""class SaleOrder(models.Model):
    product_prefix = models.CharField(max_length=20, default='PO')
    po_no = models.IntegerField("OrderNo", unique=True, blank=False, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, null=True)
    orderstatus = models.CharField('OrderStatus', max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


@receiver(post_save, sender=SaleOrder)
def set_po_no(instance, created, **_kwargs):
    if created:
        instance.po_no = instance.product_prefix + "-" + str(0000+instance.id)
"""