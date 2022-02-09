from rest_framework import serializers
from products.models import (
    Item, ProductCategory, Brand, ItemType,
    UoM1, UoM2, ItemLog, CategoryLog,
    BrandLog, UoMLog
    )


# Category Serializer
class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = '__all__'            # all Category models field(data)

# Brand Serializer
class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'

# ItemType Serializer
class ItemTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemType
        fields = '__all__'

# UoM1 Serializer
class UoM1Serializer(serializers.ModelSerializer):

    class Meta:
        model = UoM1
        fields = '__all__'


# UoM2 Serializer
class UoM2Serializer(serializers.ModelSerializer):
    class Meta:
        model = UoM2
        fields = '__all__'

# Item Serializer
class ItemSerializer(serializers.ModelSerializer):

    category = ProductCategorySerializer()
    brand = BrandSerializer()
    item_type = ItemTypeSerializer()
    uom1 = UoM1Serializer()
    uom2 = UoM2Serializer()

    class Meta :
        model = Item
        fields = '__all__'

# ItemLog Serializer
class ItemLogSerializer(serializers.ModelSerializer):

    class Meta :
        model = ItemLog
        fields = '__all__'

# CategoryLog Serializer
class CategoryLogSerializer(serializers.ModelSerializer):

    class Meta :
        model = CategoryLog
        fields = '__all__'

# BrandLog Serializer
class BrandLogSerializer(serializers.ModelSerializer):

    class Meta :
        model = BrandLog
        fields = '__all__'

# UoMLog Serializer
class UoMLogSerializer(serializers.ModelSerializer):

    class Meta :
        model = UoMLog
        fields = '__all__'
