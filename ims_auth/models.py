# import os
import datetime
import time
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from ims_auth.utils import ROLES, COUNTRIES
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


# Create Custom User models.
class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=255, unique=True)       # Email field that serves as the username field
    alternate_email = models.EmailField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    """If the user account is active or not. Defaults to True.
    If the value is set to false,user will not be allowed to sign in."""

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)                # If the user is a staff, defaults to false
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    role = models.CharField(max_length=50, choices=ROLES)
    profile_pic = models.FileField(upload_to="static/profile_pic", null=True, blank=True)
    # description = models.TextField(blank=True, null=True)

    # Setting email instead of username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = UserManager()                     # the default UserManager to make it work with our custom User Model

    def get_full_name(self):
        # Returns the first_name plus the last_name, with a space in between.
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        # Returns the short name for the user.
        return self.username

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-is_active']
        verbose_name_plural = '1. User'

    def __str__(self):
        return self.email



# Create Address models here.
class Address(models.Model):
    addresses = models.CharField("Address", max_length=255, blank=True, null=True)
    street = models.CharField("Street", max_length=55, blank=True, null=True)
    city = models.CharField("City", max_length=255, blank=True, null=True)
    state = models.CharField("State", max_length=255, blank=True, null=True)
    postcode = models.CharField("Post/Zip-code", max_length=64, blank=True, null=True)
    country = models.CharField(max_length=3, choices=COUNTRIES, blank=True, null=True)

    class Meta:
        verbose_name_plural = '3. Address'

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
    '''def get_full_address(self):
        address = ""
        if self.addresses:
            address += self.addresses
        # Returns the street plus the city plus the state plus postcode,, with a space in between.
        return f'{self.street} {self.city} {self.state} {self.postcode}'''


""" this model is used for activating the user within a particular expiration time """
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(null=True, unique=True)
    alternate_phone = PhoneNumberField(null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE,blank=True, null=True)
    role = models.CharField(max_length=50, choices=ROLES, default="USER")
    is_active = models.BooleanField(default=True)
    date_of_joining = models.DateField(null=True, blank=True)
    activation_key = models.CharField(max_length=150, null=True, blank=True)
    key_expires = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = '2. Profile'

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        """ by default the expiration time is set to 2 hours """
        self.key_expires = timezone.now() + datetime.timedelta(hours=2)
        super(Profile, self).save(*args, **kwargs)
