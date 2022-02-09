from django.urls import path
from products import views


app_name = 'products'

urlpatterns = [
    # Category Urls
    path("category-list/", views.CategoryListApiView.as_view()),
    path("category-create/", views.CategoryCreateAPIView.as_view()),
    path("category/<int:pk>/", views.CategoryAPIView.as_view()),
    path("category-delete/<int:pk>/", views.CategoryDestoryAPIView.as_view()),
    path("category-update/<int:pk>/", views.CategoryUpdateAPIView.as_view()),

    # Brand Urls
    path("brand-list/", views.BrandListApiView.as_view()),
    path("brand-create/", views.BrandCreateAPIView.as_view()),
    path("brand/<int:pk>/", views.BrandAPIView.as_view()),
    path("brand-delete/<int:pk>/", views.BrandDestoryAPIView.as_view()),
    path("brand-update/<int:pk>/", views.BrandUpdateAPIView.as_view()),

    # UoM1 Urls
    path("uom1/", views.UoM1ListCreateAPIView.as_view()),
    path("uom1/<int:pk>/", views.UoM1RetrieveUpdateDestroyAPIView.as_view()),

    # UoM2 Urls
    path("uom2/", views.UoM2ListCreateAPIView.as_view()),
    path("uom2/<int:pk>/", views.UoM2RetrieveUpdateDestroyAPIView.as_view()),

    # ItemType Urls
    path("itemtype/", views.ItemTypeListCreateAPIView.as_view()),
    path("itemtype/<int:pk>/", views.ItemTypeRetrieveUpdateDestroyAPIView.as_view()),

    # Item Urls
    path("item-list/", views.ItemListAPIView.as_view()),
    path("item/<int:pk>/", views.ItemAPIView.as_view()),
    path("item-create/", views.ItemCreateAPIView.as_view()),
    path("item-delete/<int:pk>/", views.ItemDestoryAPIView.as_view()),
    path("item-update/<int:pk>/", views.ItemUpdateAPIView.as_view()),

]
