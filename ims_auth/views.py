from django.conf import settings
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import status
from ims_auth.utils import ROLES
from django.utils.translation import gettext as _
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_encode_handler
from ims_auth.utils import jwt_payload_handler
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from .custom_auth import JSONWebTokenAuthentication
from django.db.models import Q
from rest_framework.decorators import api_view
import json
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from ims_auth.token_generator import account_activation_token
from .forms import UserForm
from ims_auth.tasks import (
    send_email_to_new_user,
    resend_activation_link_to_user,
    send_email_to_reset_password,)

from drf_yasg.utils import swagger_auto_schema
from ims_auth import swagger_params
from rest_framework.decorators import api_view
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from ims_auth.serializers import *
from ims_auth.models import *




# Create ChangePasswordAPI for User
class ChangePasswordView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        tags=["Profile"],
        operation_description="This is change password api",
        manual_parameters=swagger_params.change_password_params,
    )

    def post(self, request, format=None):
        params = request.query_params if len(
            request.data) == 0 else request.data
        context = {'user': request.user}
        serializer = PasswordChangeSerializer(data=params, context=context)
        if serializer.is_valid():
            user = request.user
            user.set_password(params.get('new_password'))
            user.save()
            return Response(
                {"error": False, "message": "Password Changed Successfully"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"error": True, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )



class LoginView(APIView):
    @swagger_auto_schema(
        tags=["Auth"],
        operation_description="This is login api",
        manual_parameters=swagger_params.login_page_params,
    )

    def post(self, request, format=None):
        params = request.query_params if len(
            request.data) == 0 else request.data
        email = params.get("email", None)
        password = params.get("password", None)
        errors = {}
        if not email:
            errors['email'] = ['This field is required']
        if not password:
            errors['password'] = ['This field is required']
        if errors:
            return Response({'error': True, 'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()
        if not user:
            return Response(
                {"error": True, "errors": "user not avaliable in our records"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not user.is_active:
            return Response(
                {"error": True, "errors": "Please activate account to proceed."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if user.check_password(password):
            payload = jwt_payload_handler(user)
            response_data = {
                "token": jwt_encode_handler(payload),
                "error": False,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            password_field = "doesnot match"
            msg = _("Email and password {password_field}")
            msg = msg.format(password_field=password_field)
            return Response(
                {"error": True, "errors": msg},
                status=status.HTTP_400_BAD_REQUEST,
            )


"""class LogoutView(LoginRequiredMixin, View):

    @swagger_auto_schema(
        tags=["Auth"],
        operation_description="This is logout api",
    )

    def get(self, request, *args, **kwargs):
        logout(request)
        request.session.flush()
        return redirect("Users:login")"""



class SignUpView(APIView):
    # model = User
    @swagger_auto_schema(
        tags=["Auth"],
        operation_description="This is registration api",
        manual_parameters=swagger_params.signup_page_params,
    )

    def post(self, request, format=None):
        params = request.query_params if len(
            request.data) == 0 else request.data

        # form = UserForm(data=params)
        form = RegisterSerializer(data=params)
        if form.is_valid():
            email = params.get('email')
            print(email)
            first_name = params.get('first_name')
            print(first_name)
            password = params.get('password')
            user, created = User.objects.get_or_create(email=email)
            print(user)


            user.first_name = first_name
            user.set_password(password)
            user.save()
            print(type(user))
            print(user)
            user.set_password(password)
            user.save()
            profile = Profile.objects.create(
                user=user,date_of_joining=timezone.now()
            )
            print(profile)
            if created:
                user.is_active = False
                user.save()
                protocol = self.request.scheme
                current_site = get_current_site(self.request)
                send_email_to_new_user.delay(
                    profile.id,
                    user.id,
                    domain=current_site.domain,
                    protocol=protocol)
                return Response(
                    {"error": False, "message": "User created Successfully."},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"error": False,
                 "message": "Please login to check the account"},
                status=status.HTTP_200_OK,
            )
        return Response({'error': True, 'errors': form.errors},
                        status=status.HTTP_400_BAD_REQUEST)



class ForgotPasswordView(APIView):
    @swagger_auto_schema(
        tags=["Auth"], manual_parameters=swagger_params.forgot_password_params
    )

    def post(self, request, format=None):
        params = request.query_params if len(
            request.data) == 0 else request.data
        serializer = ForgotPasswordSerializer(data=params)
        if serializer.is_valid():
            user = get_object_or_404(User, email=params.get("email"))
            if not user.is_active:
                return Response(
                    {"error": True, "errors": "Please activate account to proceed."},
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )
            protocol = self.request.scheme
            """send_email_to_reset_password.delay(
                user.email, protocol=protocol, domain=settings.DOMAIN_NAME
            )"""
            data = {
                "error": False,
                "message": "We have sent you an email. please reset password",
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {"error": True, "errors": serializer.errors}
            response_status = status.HTTP_400_BAD_REQUEST
        return Response(data, status=response_status)




class ResetPasswordView(APIView):
    @swagger_auto_schema(
        tags=["Auth"], manual_parameters=swagger_params.reset_password_params
    )

    def post(self, request, uid, token, format=None):
        params = request.query_params if len(
            request.data) == 0 else request.data
        try:
            uid = force_text(urlsafe_base64_decode(uid))
            user_obj = User.objects.get(pk=uid)
            if not user_obj.password:
                if not user_obj.is_active:
                    user_obj.is_active = True
                    user_obj.save()
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user_obj = None
        if user_obj is not None:
            password1 = params.get("new_password1")
            password2 = params.get("new_password2")
            if password1 != password2:
                return Response(
                    {"error": True, "errors": "The two password fields didn't match."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                user_obj.set_password(password1)
                user_obj.save()
                return Response(
                    {"error": False,
                     "message": "Password Updated Successfully. Please login"},
                    status=status.HTTP_200_OK
                )
        else:
            return Response(
                {"error": True, "errors": "Invalid Link"}
            )



class ActivateUserView(APIView):
    @swagger_auto_schema(
        tags=["Auth"],
    )
    def post(self, request, uid, token, activation_key, format=None):
        profile = get_object_or_404(Profile, activation_key=activation_key)
        if profile.user:
            if timezone.now() > profile.key_expires:
                protocol = request.scheme
                resend_activation_link_to_user.delay(
                    profile.user.email,
                    domain=settings.DOMAIN_NAME,
                    protocol=protocol,
                )
                return Response(
                    {
                        "error": False,
                        "message": "Link expired. Please use the Activation link sent now to your mail.",
                    },
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )
            else:
                try:
                    uid = force_text(urlsafe_base64_decode(uid))
                    user = User.objects.get(pk=uid)
                except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                    user = None
                if user is not None and account_activation_token.check_token(
                    user, token
                ):
                    user.is_active = True
                    user.save()
                    return Response(
                        {
                            "error": False,
                            "message": "Thank you for your email confirmation. Now you can login to your account.",
                        },
                        status=status.HTTP_200_OK,
                    )
                else:
                    return Response(
                        {"error": True, "errors": "Activation link is invalid!"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

class ResendActivationLinkView(APIView):
    @swagger_auto_schema(
        tags=["Auth"], manual_parameters=swagger_params.forgot_password_params
    )
    def post(self, request, format=None):
        params = request.query_params if len(
            request.data) == 0 else request.data
        user = get_object_or_404(User, email=params.get("email"))
        if user.is_active:
            return Response(
                {"error": False, "message": "Account is active. Please login"},
                status=status.HTTP_200_OK,
            )
        protocol = request.scheme
        resend_activation_link_to_user.delay(
            user.email,
            domain=settings.DOMAIN_NAME,
            protocol=protocol,
        )
        data = {
            "error": False,
            "message": "Please use the Activation link sent to your mail to activate account.",
        }
        return Response(data, status=status.HTTP_200_OK)