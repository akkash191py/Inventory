import re
from django.contrib.auth.hashers import check_password
from rest_framework import serializers
from .models import User, Profile, Address
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=100)

    def validate_password(self, password):
        if password:
            if len(password) < 4:
                raise serializers.ValidationError(
                    "Password must be at least 4 characters long!"
                )
        return password

    def validate_email(self, email):
        if Profile.objects.filter(user__email__iexact=email).exists():
            raise serializers.ValidationError(
                "This email is already registered")
        return email


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "alternate_email",
            "profile_pic",
            "password",
        )

    def __init__(self, *args, **kwargs):
        super(CreateUserSerializer, self).__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["password"].required = False
        self.fields["profile_pic"].required = False

    def validate_email(self, email):
        if self.instance:
            if self.instance.email != email:
                if not Profile.objects.filter(
                        user__email=email).exists():
                    return email
                raise serializers.ValidationError("Email already exists")
            return email
        else:
            if not Profile.objects.filter(user__email=email.lower()).exists():
                return email
            raise serializers.ValidationError('Given Email id already exists')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "alternate_email",
            "profile_pic",
        )



class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=200)

    def validate(self, data):
        email = data.get("email")
        user = User.objects.filter(email__iexact=email).last()
        if not user:
            raise serializers.ValidationError(
                "You don't have an account. Please create one."
            )
        return data


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=100)
    new_password = serializers.CharField(max_length=100)
    retype_password = serializers.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(PasswordChangeSerializer, self).__init__(*args, **kwargs)

    def validate_old_password(self, pwd):
        if not check_password(pwd, self.context.get('user').password):
            raise serializers.ValidationError(
                "old password entered is incorrect.")
        return pwd

    def validate(self, data):
        if len(data.get('new_password')) < 8:
            raise serializers.ValidationError(
                "Password must be at least 8 characters long!")
        if data.get('new_password') == data.get('old_password'):
            raise serializers.ValidationError(
                "New_password and old password should not be the same")
        if data.get('new_password') != data.get('retype_password'):
            raise serializers.ValidationError(
                "New_password and Retype_password did not match.")
        return data


class CheckTokenSerializer(serializers.Serializer):
    uidb64_regex = r"[0-9A-Za-z_\-]+"
    token_regex = r"[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}"
    uidb64 = serializers.RegexField(uidb64_regex)
    token = serializers.RegexField(token_regex)
    error_message = {"__all__": "Invalid password reset token"}

    def get_user(self, uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        return user


class ResetPasswordSerailizer(CheckTokenSerializer):
    new_password1 = serializers.CharField()
    new_password2 = serializers.CharField()

    def validate(self, data):
        self.user = self.get_user(data.get("uid"))
        if not self.user:
            raise serializers.ValidationError(self.error_message)
        is_valid_token = default_token_generator.check_token(
            self.user, data.get("token")
        )
        if not is_valid_token:
            raise serializers.ValidationError(self.error_message)
        new_password2 = data.get("new_password2")
        new_password1 = data.get("new_password1")
        if new_password1 != new_password2:
            raise serializers.ValidationError(
                "The two password fields didn't match.")
        return new_password2

class AddressSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()

    def get_country(self, obj):
        return obj.get_country_display()

    class Meta:
        model = Address
        fields = ("addresses", "street", "city",
                  "state", "postcode", "country")

    def __init__(self, *args, **kwargs):
        account_view = kwargs.pop("account", False)

        super(AddressSerializer, self).__init__(*args, **kwargs)

        if account_view:
            self.fields["addresses"].required = True
            self.fields["street"].required = True
            self.fields["city"].required = True
            self.fields["state"].required = True
            self.fields["postcode"].required = True
            self.fields["country"].required = True


class CreateProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            "role",
            "phone",
            "alternate_phone",
        )

    def __init__(self, *args, **kwargs):
        super(CreateProfileSerializer, self).__init__(*args, **kwargs)
        self.fields["alternate_phone"].required = False
        self.fields["role"].required = True
        self.fields["phone"].required = True




class ProfileSerializer(serializers.ModelSerializer):
    user_details = serializers.SerializerMethodField()
    address = AddressSerializer()

    def get_user_details(self, obj):
        return UserSerializer(obj.user).data

    class Meta:
        model = Profile
        fields = ("id", 'user_details', 'role', 'address',
                  'phone', 'date_of_joining', 'is_active')

