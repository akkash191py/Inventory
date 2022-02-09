#from django.contrib.auth import views as auth_views
from django.urls import path
from profiles import views


app_name = 'profiles'

urlpatterns = [
    path("profile/", views.ProfileView.as_view()),
    path("users/<int:pk>/", views.UserDetailView.as_view()),
    path("users/", views.UsersListView.as_view()),
]
