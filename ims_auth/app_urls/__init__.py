from django.urls import include, path

app_name = "ims_auth_urls"
urlpatterns = [
    path("", include(('ims_auth.urls'))),
    path("", include(('profiles.urls'))),
    path("", include(('products.urls'))),
    path("", include(('stock_mg.urls'))),
    path("", include(('inventory_manage.urls'))),
]