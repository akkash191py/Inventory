from django.urls import path
from inventory_manage import views


app_name = 'inventory_manage'

urlpatterns = [
    # Purchase Urls
    path("purchase-item-list/", views.PurchaseList.as_view()),
    path("purchase-item/<int:pk>/", views.PurchaseAPIView.as_view()),
    path("purchase-item-create/", views.PurchaseCreate.as_view()),
    path("purchase-item-delete/<int:pk>/", views.PurchaseAPIView.as_view()),
    path("purchase-update/<int:pk>/", views.PurchaseUpdateView.as_view()),
]