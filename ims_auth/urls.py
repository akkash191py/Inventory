#from django.contrib.auth import views as auth_views
from django.urls import path
from ims_auth import views


"""from Users.views import (LoginView,SignUpView,
    ChangePasswordView, ForgotPasswordView, ResetPasswordView
    )"""

app_name = 'ims_auth'

urlpatterns = [

    path('auth/SignUp/', views.SignUpView.as_view()),
    path("auth/login/", views.LoginView.as_view()),
    path("profile/change-password/", views.ChangePasswordView.as_view()),
    path("auth/forgot-password/", views.ForgotPasswordView.as_view()),
    path("auth/reset-password/<str:uid>/",views.ResetPasswordView.as_view(),),

    path(
        "auth/activate-user/<str:uid>/<str:token>/<str:activation_key>/",
        views.ActivateUserView.as_view(),),

    path("auth/resend-activation-link/", views.ResendActivationLinkView.as_view()),

]

