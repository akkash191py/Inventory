from django.contrib import admin
from products.models import (
    ProductCategory,CategoryLog, UoM1, UoM2, UoMLog,
    ItemType, Brand, BrandLog, Item, ItemLog, MultiImage,
    )
from import_export.admin import ImportExportModelAdmin

# CustomerAdmin models.
"""class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'address', 'date_created')
admin.site.register(Customer, CustomerAdmin)
"""

# Category ImportExport Model Admin
"""class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('name', 'parent', 'description')
    list_filter = ('name', )
admin.site.register(Category, CategoryAdmin)"""
#admin.site.register(Category)

class ProductCategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'parentCategory', 'description', 'created_by', 'created_at')
admin.site.register(ProductCategory, ProductCategoryAdmin)

class CategoryLogAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'modify_by', 'modify_on', 'details')
admin.site.register(CategoryLog, CategoryLogAdmin)

class UoM1Admin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'short_name', 'created_by', 'created_at')
admin.site.register(UoM1, UoM1Admin)

class UoM2Admin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'short_name', 'created_by', 'created_at')
admin.site.register(UoM2, UoM2Admin)

class UoMLogAdmin(ImportExportModelAdmin):
    list_display = ('id', 'Uom1', 'Uom2', 'modify_by', 'modify_on', 'details')
admin.site.register(UoMLog, UoMLogAdmin)

# BrandAdmin models.
class BrandAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'logo', 'description', 'created_by', 'created_on')
    list_filter = ('name', )
admin.site.register(Brand, BrandAdmin)
admin.site.register(ItemType)

class BrandLogAdmin(ImportExportModelAdmin):
    list_display = ('id', 'brand', 'modify_by', 'modify_on', 'details')
admin.site.register(BrandLog, BrandLogAdmin)


# ProductAdmin models.
class ItemAdmin(ImportExportModelAdmin):
    list_display = ('id', 'sku', 'barcode', 'name', 'category', 'brand', 'item_type', 'uom1', 'uom2', 'short_details', 'status')
    list_filter = ('category', 'brand', 'name', 'item_type',)
    search_fields = ['sku', 'barcode', 'name', 'category__name', 'brand__name']
    list_per_page = 15
admin.site.register(Item, ItemAdmin)

class ItemLogAdmin(ImportExportModelAdmin):
    list_display = ('id', 'parent_item', 'last_modify', 'description')
admin.site.register(ItemLog, ItemLogAdmin)

admin.site.register(MultiImage)

# CustomerAdmin models.
"""class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')
admin.site.register(Category, CategoryAdmin)

# BrandAdmin models.
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_name', 'brand_code', 'img')
admin.site.register(Brand, BrandAdmin)

# ProductAdmin models.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'code', 'name', 'quantity', 'price', 'image', 'status')
admin.site.register(Product, ProductAdmin)
"""

