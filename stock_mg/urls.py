from django.urls import path
from stock_mg import views


app_name = 'stock_mg'

urlpatterns = [
    # ReceiveItem Urls
    path("receive_item-list/", views.StockReceiveList.as_view()),
    path("receive-item/<int:pk>/", views.StockReceiveAPIView.as_view()),
    path("receive_item-create/", views.StockReceiveCreate.as_view()),
    path("receive-item-delete/<int:pk>/", views.StockReceiveAPIView.as_view()),
    path("receive-update/<int:pk>/", views.StockReceiveAPIView.as_view()),

    # IssueItem Urls
    path("issue-item-list/", views.StockIssueList.as_view()),
    path("issue-item/<int:pk>/", views.StockIssueAPIView.as_view()),
    path("issue_item-create/", views.StockIssueCreate.as_view()),
    path("issue-item-delete/<int:pk>/", views.StockIssueView.as_view()),
    path("issue-update/<int:pk>/", views.StockIssueUpdate.as_view()),


    # TotalIn Urls
    path("total-qty-list/", views.TotalInList.as_view()),
    path("total-qty-item/<int:pk>/", views.TotalInView.as_view()),

    # TotalOut Urls
    path("total-issue-qty-list/", views.TotalOutList.as_view()),
    path("total-issue-qty-item/<int:pk>/", views.TotalOutView.as_view()),

]
