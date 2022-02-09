from django.contrib import admin
from clients.models import Customer, Vendor, AlternateAddr

# Customer Admin Model
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id", "customer_no", "name", "email", "phone", "address"]
    list_filter = ["customer_no", "name"]
    search_fields = ["customer_no", "name"]
admin.site.register(Customer, CustomerAdmin)

# Vendor Admin Model
class VendorAdmin(admin.ModelAdmin):
    list_display = ["id", "vendor_no", "name", "email", "phone", "address"]
    list_filter = ["vendor_no", "name"]
    search_fields = ["vendor_no", "name"]
admin.site.register(Vendor, VendorAdmin)

admin.site.register(AlternateAddr)