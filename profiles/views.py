from django.shortcuts import render
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404, redirect
from rest_framework import status
from ims_auth.serializers import *
from ims_auth.utils import ROLES, COUNTRIES
from ims_auth.models import User,  Profile, Address
from ims_auth.tasks import (
    send_email_to_new_user,
    resend_activation_link_to_user,
    # send_email_user_delete,
    # send_email_user_status,
    send_email_to_reset_password,
)
from django.utils.translation import gettext as _
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_encode_handler
from ims_auth.utils import jwt_payload_handler
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from ims_auth.custom_auth import JSONWebTokenAuthentication
from ims_auth import swagger_params
from django.db.models import Q
from rest_framework.decorators import api_view
import json
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from ims_auth.token_generator import account_activation_token
from django.utils import timezone
from django.conf import settings


# Create your views here.

class ProfileView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        tags=["Profile"]
    )
    def get(self, request, format=None):
        context = {}
        context["user_obj"] = ProfileSerializer(request.profile).data
        return Response(context, profile, status=status.HTTP_200_OK)



class UserDetailView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        profile = get_object_or_404(Profile, pk=pk)
        return profile

    @swagger_auto_schema(
        tags=["Users"]
    )
    def get(self, request, pk, format=None):
        user_obj = self.get_object(pk)
        print(user_obj)
        """if (
                self.request.profile.role != "ADMIN"
                and not self.request.profile.is_admin
                and self.request.profile.id != profile_obj.id
        ):
            return Response(
                {"error": True, "errors": "Permission Denied"},
                status=status.HTTP_403_FORBIDDEN,
            )"""

        users_data = []
        for each in Profile.objects.all():
            assigned_dict = {}
            assigned_dict["id"] = each.id
            assigned_dict["name"] = each.user.first_name
            users_data.append(assigned_dict)
        context = {}
        context["user_obj"] = ProfileSerializer(user_obj).data
        context["assigned_data"] = users_data
        context["countries"] = COUNTRIES
        return Response(
            {"error": False, "data": context},
            status=status.HTTP_200_OK, )



    @swagger_auto_schema(
        tags=["Users"], manual_parameters=swagger_params.user_update_params
    )
    def put(self, request, pk, format=None):
        params = request.query_params if len(
            request.data) == 0 else request.data
        profile = self.get_object(pk)
        address_obj = profile.address
        if (
            self.request.profile.role != "ADMIN"
            and not self.request.user.is_admin
            and self.request.profile.id != profile.id
        ):
            return Response(
                {"error": True, "errors": "Permission Denied"},
                status=status.HTTP_403_FORBIDDEN,
            )
        serializer = CreateUserSerializer(
            data=params, instance=profile.user)
        address_serializer = AddressSerializer(
            data=params, instance=address_obj)
        profile_serializer = CreateProfileSerializer(
            data=params, instance=profile)
        data = {}
        if not serializer.is_valid():
            data["contact_errors"] = serializer.errors
        if not address_serializer.is_valid():
            data["address_errors"] = (address_serializer.errors,)
        if not profile_serializer.is_valid():
            data["profile_errors"] = (profile_serializer.errors,)
        if data:
            data["error"] = True
            return Response(
                data,
                status=status.HTTP_400_BAD_REQUEST,
            )
        if serializer.is_valid():
            address_obj = address_serializer.save()
            user = serializer.save()
            user.username = user.first_name
            user.save()
            profile = profile_serializer.save()
            return Response(
                {"error": False, "message": "User Updated Successfully"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"error": True, "errors": "serializer.errors"},
            status=status.HTTP_400_BAD_REQUEST,
        )


    @swagger_auto_schema(
        tags=["Users"]
    )
    def delete(self, request, pk, format=None):
        if self.request.profile.role != "ADMIN" and not self.request.profile.is_admin:
            return Response(
                {"error": True, "errors": "Permission Denied"},
                status=status.HTTP_403_FORBIDDEN,
            )
        self.object = self.get_object(pk)
        if self.object.id == request.profile.id:
            return Response(
                {"error": True, "errors": "Permission Denied"},
                status=status.HTTP_403_FORBIDDEN,
            )
        deleted_by = self.request.profile.user.email
        self.object.delete()
        return Response({"status": "success"}, status=status.HTTP_200_OK)


class UsersListView(APIView, LimitOffsetPagination):

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        tags=["Users"], manual_parameters=swagger_params.user_create_params
    )
    def post(self, request, format=None):
        if self.request.profile.role != "ADMIN" and not self.request.user.is_superuser:
            return Response(
                {"error": True, "errors": "Permission Denied"},
                status=status.HTTP_403_FORBIDDEN,
            )
        else:
            params = request.query_params if len(
                request.data) == 0 else request.data
            if params:
                user_serializer = CreateUserSerializer(
                    data=params)
                address_serializer = AddressSerializer(data=params)
                profile_serializer = CreateProfileSerializer(data=params)
                data = {}
                if not user_serializer.is_valid():
                    data["user_errors"] = dict(user_serializer.errors)
                if not profile_serializer.is_valid():
                    data['profile_errors'] = profile_serializer.errors
                if not address_serializer.is_valid():
                    data["address_errors"] = (address_serializer.errors,)
                if data:
                    return Response(
                        {"error": True, "errors": data},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                if user_serializer.is_valid():
                    address_obj = address_serializer.save()
                    user = user_serializer.save(
                        is_active=False,
                    )
                    user.username = user.first_name
                    user.save()
                    if params.get("password"):
                        user.set_password(params.get("password"))
                        user.save()
                    profile = Profile.objects.create(user=user,
                                                     date_of_joining=timezone.now(),
                                                     role=params.get(
                                                         'role'),
                                                     address=address_obj,
                                                     ),

                    current_site = get_current_site(self.request)
                    protocol = request.scheme
                    send_email_to_new_user.delay(
                        profile[0].id,
                        request.org.id,
                        domain=current_site.domain,
                        protocol=protocol,
                    )
                    return Response(
                        {"error": False, "message": "User Created Successfully"},
                        status=status.HTTP_201_CREATED,
                    )
