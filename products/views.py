# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    )
from products.models import Item, ProductCategory, Brand, UoM1, UoM2, ItemType
from products.serializers import (
    ItemSerializer,
    ProductCategorySerializer,
    BrandSerializer,
    ItemTypeSerializer,
    UoM1Serializer,
    UoM2Serializer,
    )
# from drf_yasg.utils import swagger_auto_schema
# from rest_framework.permissions import IsAuthenticated       # its required but now just testing api w/o authenticate
# from ims_auth.custom_auth import JSONWebTokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from products.filterset import ItemFilter
# from django_filters import rest_framework as filters
from rest_framework import filters
from googletrans import Translator

translator = Translator()



# ListAPI View of Product-Category.
class CategoryListApiView(ListAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = ProductCategorySerializer
    filter_backends = (DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ("name")
    # ordering_fields = ("created_at")
    queryset = ProductCategory.objects.all()



# RetrieveAPI View of Product_Category
class CategoryAPIView(RetrieveAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = {}
        for k, v in serializer.data.items():
            data = translator.translate(str(v), dest='ar').text

        return Response(data)


# CreateAPI View of Product-Category.
class CategoryCreateAPIView(CreateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()

# DestroyAPI View of Product-Category.
class CategoryDestoryAPIView(DestroyAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response({"detail": "Product-Category deleted"})


# UpdateAPI View of Product-Category.
class CategoryUpdateAPIView(UpdateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()


# ListAPI View of Brand.
class BrandListApiView(ListAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = BrandSerializer
    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter,
                       )
    search_fields = ("name")
    ordering_fields = ("created_on")
    queryset = Brand.objects.all()


# RetrieveAPI View of Brand.
class BrandAPIView(RetrieveAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = {}
        for k, v in serializer.data.items():
            data = translator.translate(str(v), dest='ar').text

        return Response(data)


# CreateAPI View of Brand.
class BrandCreateAPIView(CreateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


# DestroyAPI View of Brand.
class BrandDestoryAPIView(DestroyAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response({"detail": "Brand deleted"})


# UpdateAPI View of Brand.
class BrandUpdateAPIView(UpdateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


# ListCreateAPIView for UoM1
class UoM1ListCreateAPIView(ListCreateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = UoM1Serializer
    queryset = UoM1.objects.all()

# Retrieve Update Destroy APIView for UoM1
class UoM1RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = UoM1Serializer
    queryset = UoM1.objects.all()

# ListCreateAPIView for UoM2
class UoM2ListCreateAPIView(ListCreateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = UoM2Serializer
    queryset = UoM2.objects.all()

# Retrieve Update Destroy APIView for UoM1
class UoM2RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = UoM2Serializer
    queryset = UoM2.objects.all()

# ListCreateAPIView for ItemType
class ItemTypeListCreateAPIView(ListCreateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = ItemTypeSerializer
    queryset = ItemType.objects.all()

# Retrieve Update Destroy APIView for ItemType
class ItemTypeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = ItemTypeSerializer
    queryset = ItemType.objects.all()




# Create your views here.
class ItemListAPIView(ListAPIView):

    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_class = ItemFilter

    search_fields = ("name", "sku", "barcode","category","brand")
    ordering_fields = ("created_on")

    """def get(self, request):
        category = self.request.query_params.get('category')
        if category:
            queryset = Item.objects.filter(category__name=category)
        else:
            queryset = Item.objects.all()
        serializer = ItemSerializer(queryset, many=True)
        return Response({'count': len(serializer.data), 'data': serializer.data})"""



# RetrieveAPI View of Item.
class ItemAPIView(RetrieveAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


# CreateAPI View of Item.
class ItemCreateAPIView(CreateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


# DestroyAPI View of Item.
class ItemDestoryAPIView(DestroyAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response({"detail": "One Item deleted"})


# UpdateAPI View of Item.
class ItemUpdateAPIView(UpdateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
