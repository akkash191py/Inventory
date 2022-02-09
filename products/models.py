from __future__ import unicode_literals
import arrow
from django.db import models
from ims_auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField
from products.utils import PRODUCT_STATUS, CODE_TYPE







# Category
class ProductCategory(models.Model):
    parentCategory = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    # active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)



    class Meta:
        verbose_name_plural = '1. Product Category'

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of ProductCategory.
        """
        return reverse('category-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name or self.parentCategory

# Category Log
class CategoryLog(models.Model):
    name = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=True, null=True)
    modify_by = models.CharField(max_length=50, blank=True, null=True)
    modify_on = models.DateTimeField(auto_now=True, editable=False)
    details = models.CharField(max_length=500)



    class Meta:
        verbose_name_plural = '7. Category Log'

    def __str__(self):
        return str(self.name)

# Unit of Measure 1
class UoM1(models.Model):
    name = models.CharField("Unit of Measure", max_length=50, blank=True, null=True)
    short_name = models.CharField("UoM", max_length=10, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)


    class Meta:
        verbose_name_plural = '4. Uom1'

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Unit of Measure.
        """
        return reverse('uom1-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name

# Unit of Measure 2
class UoM2(models.Model):
    name = models.CharField("Unit of Measure", max_length=50, blank=True, null=True)
    short_name = models.CharField("UoM", max_length=10, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)


    class Meta:
        verbose_name_plural = '5. Uom2'

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Unit of Measure.
        """
        return reverse('uom2-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.short_name

# UoM Log
class UoMLog(models.Model):
    Uom1 = models.ForeignKey(UoM1,related_name= "UOM1", on_delete=models.CASCADE, blank=True, null=True)
    Uom2 = models.ForeignKey(UoM1,related_name= "UOM2", on_delete=models.CASCADE, blank=True, null=True)
    modify_by = models.CharField(max_length=50, blank=True, null=True)
    modify_on = models.DateTimeField(auto_now=True, editable=False)
    details = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = '9. Uom Log'

    def __str__(self):
        return str(self.Uom1 or self.Uom2)

# Brand Model
class Brand(models.Model):
    name = models.CharField("Brand name", max_length=100)
    logo = models.ImageField(upload_to='static/brands')
    description = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name_plural = '2. Brands '

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Brand.
        """
        return reverse('brand-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name


class BrandLog(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    modify_by = models.CharField(max_length=50, blank=True, null=True)
    modify_on = models.DateTimeField(auto_now=True, editable=False)
    details = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = '8. Brand Log'


    def __str__(self):
        return self.brand

class ItemType(models.Model):
    name = models.CharField("Item Type", max_length=100, blank=True, null=True)


    class Meta:
        verbose_name_plural = '3. Item Type '

    def __str__(self):
        return self.name


class ItemTypeLog(models.Model):
    brand = models.ForeignKey(ItemType, on_delete=models.CASCADE, blank=True, null=True)
    modify_by = models.CharField(max_length=50, blank=True, null=True)
    modify_on = models.DateTimeField(auto_now=True, editable=False)
    details = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = '9. ItemType Log'



"""class ItemAttributeCode(models.Model):
    code_type = models.CharField("Code Type", max_length=30, choices=CODE_TYPE)
    sku = models.CharField("SKU", max_length=13, unique=True, help_text="Enter Product Stock Keeping Unit")
    barcode = models.CharField(max_length=13, unique=True, help_text="Enter Product Barcode (ISBN, UPC ...)")
"""


class ItemManager(models.Manager):
    def active(self):
        return self.filter(active=True)

    """def have_qty(self):
        return self.active.filter(qty__gte=1)"""


class Item(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField("Item name", max_length=100, unique=True)
    code_type = models.CharField("Code Type", max_length=30, choices=CODE_TYPE)
    sku = models.CharField("SKU", max_length=13, unique=True, help_text="Enter Product Stock Keeping Unit")
    barcode = models.CharField(max_length=13, unique=True, help_text="Enter Product Barcode (ISBN, UPC ...)")
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True)
    item_type = models.ForeignKey(ItemType, related_name="Itemtype", on_delete=models.CASCADE, blank=True, null=True)
    uom1 = models.ForeignKey(UoM1, on_delete=models.SET_NULL, blank=True, null=True)
    uom2 = models.ForeignKey(UoM2, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField(max_length= 150, blank=True, null=True)
    short_details = models.TextField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, choices=PRODUCT_STATUS, default="Available")
    active = models.BooleanField(default=True)
    # created_by = models.CharField(max_length=50, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    last_log = models.ForeignKey('ItemLog', null=True, blank=True, default=None, on_delete=models.SET_NULL)

    objects = models.Manager()
    broswer = ItemManager()


    class Meta:
        # verbose_name = _('Item')
        verbose_name_plural = '6. Items '
        ordering = ("-created_on", )

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Item.
        """
        return reverse('product-detail-view', args=[str(self.id)])

    def __str__(self):
        return (self.name)

    @property
    def created_on_arrow(self):
        return arrow.get(self.created_on).humanize()



class ItemLog(models.Model):
    # user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    parent_item = models.ForeignKey(Item, null=True, blank=True, on_delete=models.CASCADE)
    last_modify = models.DateTimeField(auto_now=True, editable=False)
    description = models.CharField(max_length=200, null=True)
    # item_no = models.CharField("item code", max_length=13, help_text="Enter Product Stock Keeping Unit")
    # item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)
    # modify_by = models.CharField(max_length=50, blank=True, null=True)


    class Meta:
        verbose_name_plural = 'Item Log'



class MultiImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)
    image1 = models.ImageField(upload_to='static/products', blank=True, null=True)
    image2 = models.ImageField(upload_to='static/products', blank=True, null=True)
    image3 = models.ImageField(upload_to='static/products', blank=True, null=True)
    image4 = models.ImageField(upload_to='static/products', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Item Images'