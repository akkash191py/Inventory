from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView
)
from stock_mg.models import StockReceive, StockIssue, totalinstock, totaloutstock

# from products.models import Product, Category, Brand
# from products.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from ims_auth.custom_auth import JSONWebTokenAuthentication
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from stock_mg.filterset import StockReceiveFilter, StockIssueFilter, totalinstockFilter, totaloutstockFilter
from stock_mg.serializers import (
    StockReceiveSerializer,
    StockIssueSerializer,
    totalinstockSerializer,
    totaloutstockSerializer,
    )
from django_filters import rest_framework as filters


# StockListviews here.
class StockReceiveList(ListAPIView):

    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    # item_count = StockReceive.objects.all().count()
    queryset = StockReceive.objects.all()
    serializer_class = StockReceiveSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = StockReceiveFilter



# StockReceiveCreateviews here.
class StockReceiveCreate(CreateAPIView):

    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = StockReceive.objects.all()
    serializer_class = StockReceiveSerializer


# RetrieveAPI View of StockReceive.
class StockReceiveAPIView(RetrieveAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = StockReceiveSerializer
    queryset = StockReceive.objects.all()


# DestroyAPI View of StockReceive.
class StockReceiveAPIView(DestroyAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = StockReceiveSerializer
    queryset = StockReceive.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response({"detail": "One Received Item deleted"})

# UpdateAPI View of StockReceive.
class StockReceiveAPIView(UpdateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = StockReceiveSerializer
    queryset = StockReceive.objects.all()



# StockIssueListviews here.
class StockIssueList(ListAPIView):

    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    # item_count = StockReceive.objects.all().count()
    queryset = StockIssue.objects.all()
    serializer_class = StockIssueSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = StockIssueFilter



# StockIssue Createviews here.
class StockIssueCreate(CreateAPIView):

    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = StockIssue.objects.all()
    serializer_class = StockIssueSerializer


# RetrieveAPI View of StockIssue.
class StockIssueAPIView(RetrieveAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = StockIssueSerializer
    queryset = StockIssue.objects.all()


# DestroyAPI View of StockReceive.
class StockIssueView(DestroyAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = StockIssueSerializer
    queryset = StockIssue.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response({"detail": "One Received Item deleted"})

# UpdateAPI View of StockIssue.
class StockIssueUpdate(UpdateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = StockIssueSerializer
    queryset = StockIssue.objects.all()



# Totalinstock Listviews here.
class TotalInList(ListAPIView):

    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    # item_count = StockReceive.objects.all().count()
    queryset = totalinstock.objects.all()
    serializer_class = totalinstockSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = totalinstockFilter


# RetrieveAPI View of Totalinstock.
class TotalInView(RetrieveAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = totalinstockSerializer
    queryset = totalinstock.objects.all()


# Totalinstock Listviews here.
class TotalOutList(ListAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    # item_count = StockReceive.objects.all().count()
    queryset = totaloutstock.objects.all()
    serializer_class = totaloutstockSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = totaloutstockFilter


# RetrieveAPI View of Totaloutstock.
class TotalOutView(RetrieveAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = totaloutstockSerializer
    queryset = totaloutstock.objects.all()


# StockUpdateviews here.
'''class StockUpdate(UpdateAPIView):

    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Stock.objects.all()
    serializer_class = StockUpdateSerializer
'''

# StockRetrieveviews here.
'''class StockRetrieve(RetrieveAPIView):

    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
'''

# StockDestroyAPIView here.
'''class StockDestroy(DestroyAPIView):

    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
'''

'''class Issueitems(UpdateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Stock.objects.all()
    serializer_class = IssueSerializer
'''
""" def get_serializer_class(self):
        return IssueSerializer
    
    def post(self,request, format=None):

        serializer = IssueSerializer(request.data)
        if serializer.is_valid():

            instance = serializer.save(commit=False)
            instance.quantity -=instance.issue_quantity
            # instance.issue_by = Stock.issue_by
            message = []
            message.success("Issued SUCCESSFULLY." + str(instance.quantity) + " "
                         + str(instance.items)
                         + "s now left in store")
            instance.save()
            return Response(
                {"error": False, "message": "User Created Successfully"},
                status=status.HTTP_201_CREATED,
            )"""

'''class Receiveitems(UpdateAPIView):
    queryset = Stock.objects.all()
    serializer_class = ReceiveSerializer

class ReceiveList(ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = ReceiveSerializer
'''


'''class ReorderLevel(UpdateAPIView):
    queryset = Stock.objects.all()
    serializer_class = ReorderLevelSerializer'''
""" if serializer.is_s:
        instance = serializer.save(commit=False)
        instance.save()
        messages.success(request, "Reorder level for "
                         + str(instance.item_name)+ " is updated to "
                         + str(instance.reorder_level))

        return Response(
            {"error": False, "message": "Receive Stock Successfully"},
            status=status.HTTP_201_CREATED,
        )"""
