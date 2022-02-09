from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from inventory_manage.models import Purchase, Sale, Inventory, Customer, Vendor
from django_filters import rest_framework as filters
from inventory_manage.filterset import PurchaseFilter
from inventory_manage.serializers import (
    PurchaseSerializer,
    SaleSerializer,
)


# Purchase Listviews here.
class PurchaseList(ListAPIView):

    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    # item_count = Purchase.objects.all().count()
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PurchaseFilter



# PurchaseSerializer Createviews here.
class PurchaseCreate(CreateAPIView):

    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


# RetrieveAPI View of Purchase.
class PurchaseAPIView(RetrieveAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()


# DestroyAPI View of Purchase.
class PurchaseAPIView(DestroyAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response({"detail": "One Purchased Item deleted"})

# UpdateAPI View of Purchase.
class PurchaseUpdateView(UpdateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()

