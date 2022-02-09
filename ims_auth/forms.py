from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import authenticate
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from ims_auth.models import User
# from teams.models import Teams

# Create Form for User .
class UserForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
        fields, plus a repeated password."""
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password1 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name',
                  'username', 'role', 'profile_pic']

    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop('request_user', None)
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        if not self.instance.pk:
            self.fields['password'].required = True


    def clean_password1(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password and password1 and password != password1:
            raise ValidationError("Passwords don't match")
        # return password1

        if password:
            if len(password) < 4:
                raise forms.ValidationError(
                    'Password must be at least 4 characters long!')
        return password


    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


    def clean_email(self):
        email = self.cleaned_data.get("email")
        if self.instance.id:
            if self.instance.email != email:
                if not User.objects.filter(
                        email=self.cleaned_data.get("email")).exists():
                    return self.cleaned_data.get("email")
                raise forms.ValidationError('Email already exists')
            else:
                return self.cleaned_data.get("email")
        else:
            if not User.objects.filter(
                    email=self.cleaned_data.get("email")).exists():
                return self.cleaned_data.get("email")
            raise forms.ValidationError('User already exists with this email')


# Create LoginForm for User
"""class LoginForm(forms.ModelForm):
    # A form for login to users
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']


    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(LoginForm, self).__init__(*args, **kwargs)


    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            if len(password) < 4:
                raise forms.ValidationError(
                    'Password must be at least 4 characters long!')
        return password

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(username=email, password=password)
            if self.user:
                if not self.user.is_active:
                    pass
                    # raise forms.ValidationError("User is Inactive")
            else:
                pass
                # raise forms.ValidationError("Invalid email and password")
        return self.cleaned_data



# Create ChangePasswordForm for User
class ChangePasswordForm(forms.Form):
    # CurrentPassword = forms.CharField(max_length=100)
    Newpassword = forms.CharField(max_length=100)
    confirm = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    def clean_confirm(self):
        # if len(self.data.get('confirm')) < 4:
        #     raise forms.ValidationError(
        #         'Password must be at least 4 characters long!')
        if self.data.get('confirm') != self.cleaned_data.get('Newpassword'):
            raise forms.ValidationError(
                'Confirm password do not match with new password')
        password_validation.validate_password(
            self.cleaned_data.get('Newpassword'), user=self.user)
        return self.data.get('confirm')



# Create PasswordResetEmailForm for User
class PasswordResetEmailForm(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email__iexact=email,
                                   is_active=True).exists():
            raise forms.ValidationError("User doesn't exist with this Email")
        return email

"""