import arrow
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ims_auth.models import User, Address
from ims_auth.utils import COUNTRIES
# Create your models here.

# Alternate Address
class AlternateAddr(models.Model):
    addresses = models.CharField("Address", max_length=255, blank=True, null=True)
    street = models.CharField("Street", max_length=55, blank=True, null=True)
    city = models.CharField("City", max_length=255, blank=True, null=True)
    state = models.CharField("State", max_length=255, blank=True, null=True)
    postcode = models.CharField("Post/Zip-code", max_length=64, blank=True, null=True)
    country = models.CharField(max_length=3, choices=COUNTRIES, blank=True, null=True)

    class Meta:
        verbose_name_plural = '1. Alternate Address'

    def __str__(self):
        return self.city if self.city else ""

    def get_complete_address(self):
        address = ""
        if self.addresses:
            address += self.addresses

        if self.street:
            if address:
                address += ", " + self.street
            else:
                address += self.street
        if self.city:
            if address:
                address += ", " + self.city
            else:
                address += self.city
        if self.state:
            if address:
                address += ", " + self.state
            else:
                address += self.state
        if self.postcode:
            if address:
                address += ", " + self.postcode
            else:
                address += self.postcode

        if self.country:
            if address:
                address += ", " + self.get_country_display()
            else:
                address += self.get_country_display()
        return address


# Customer Model.
class Customer(models.Model):
    customer_no = models.CharField("Customer id", unique=True, max_length=20, null=True)
    name = models.CharField("Customer name", max_length=100, null=True)
    email = models.EmailField(max_length=25, null=True)
    phone = PhoneNumberField(null=True, unique=True)
    alternate_phone = PhoneNumberField(null=True)
    date_created = models.DateTimeField(editable=False, auto_now_add=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
    alternate_address = models.ForeignKey(AlternateAddr, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = "2. Customer"

    def __str__(self):
        return self.name

    @property
    def created_on_arrow(self):
        return arrow.get(self.date_created).humanize()

# Vendor Model.
class Vendor(models.Model):
    vendor_no = models.CharField("Vendor id", unique=True, max_length=20, null=True)
    name = models.CharField("Vendor name", max_length=100, null=True)
    email = models.EmailField(max_length=25, null=True)
    phone = PhoneNumberField(null=True, unique=True)
    alternate_phone = PhoneNumberField(null=True)
    date_created = models.DateTimeField(editable=False, auto_now_add=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
    alternate_address = models.ForeignKey(AlternateAddr, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = "3. vendor"

    def __str__(self):
        return self.name

    @property
    def created_on_arrow(self):
        return arrow.get(self.date_created).humanize()