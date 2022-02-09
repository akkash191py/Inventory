import datetime
from celery import Celery
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils import six, timezone
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from celery import shared_task
from .models import User, Profile, Address
from ims_auth.token_generator import account_activation_token
from django.contrib.auth.tokens import default_token_generator


# app = Celery("redis://")

@shared_task
def send_email_to_new_user(profile_id, user_id, domain="demo.django-crm.io", protocol="http"):
    """ Send Mail To Users When their account is created """

    profile_obj = Profile.objects.filter(id=profile_id).last()
    user = User.objects.filter(id=user_id).first()
    print(profile_obj)
    print(user)
    print(profile_obj.id)
    print(profile_obj.pk)
    print(profile_obj.__dict__)

    user_obj = profile_obj.user
    if profile_obj:
        context = {}
        user_email = user.email
        context["url"] = protocol + '://' + domain
        context["uid"] = (urlsafe_base64_encode(force_bytes(user_obj.pk)),)
        context["token"] = account_activation_token.make_token(user_obj)
        print(context["uid"])
        print(context["token"])
        time_delta_two_hours = datetime.datetime.strftime(
            timezone.now() + datetime.timedelta(hours=2), "%Y-%m-%d-%H-%M-%S")
        activation_key = context["token"] + time_delta_two_hours
        print(activation_key)
        # user_obj.activation_key = activation_key
        profile_obj.activation_key = activation_key
        profile_obj.save()
        # user_obj.save()
        context["complete_url"] = context["url"] + "/auth/activate-user/{}/{}/{}/".format(
                context['uid'][0], context['token'], activation_key,)
        # context["complete_url"] = complete_url
        recipients = []
        recipients.append(user_email)
        subject = 'Welcome to Inventory'

        html_content = render_to_string("user_status_in.html", context=context)
        if recipients:
            msg = EmailMessage(
                subject,
                html_content,
                from_email=settings.EMAIL_HOST_USER,
                to=recipients
            )
            msg.content_subtype = "html"
            msg.send()


@shared_task
def resend_activation_link_to_user(
    user_email="", domain="demo.django-crm.io", protocol="http"):
    """ Send Mail To Users When their account is created """

    user_obj = User.objects.filter(email=user_email).first()
    user_obj.is_active = False
    user_obj.save()
    if user_obj:
        context = {}
        context["user_email"] = user_email
        context["url"] = protocol + "://" + domain
        context["uid"] = (urlsafe_base64_encode(force_bytes(user_obj.pk)),)
        context["token"] = account_activation_token.make_token(user_obj)
        time_delta_two_hours = datetime.datetime.strftime(
            timezone.now() + datetime.timedelta(hours=2), "%Y-%m-%d-%H-%M-%S"
        )
        context["token"] = context["token"]
        activation_key = context["token"] + time_delta_two_hours
        Profile.objects.filter(user=user_obj).update(
            activation_key=activation_key,
            key_expires=timezone.now() + datetime.timedelta(hours=2),
        )
        context["complete_url"] = context[
            "url"
        ] + "/auth/activate_user/{}/{}/{}/".format(
            context["uid"][0],
            context["token"],
            activation_key,
        )
        recipients = []
        recipients.append(user_email)
        subject = "Welcome to Django CRM"
        html_content = render_to_string(context=context)
        if recipients:
            msg = EmailMessage(subject, html_content, from_email=settings.EMAIL_HOST_USER, to=recipients)
            msg.content_subtype = "html"
            msg.send()



@shared_task
def send_email_to_reset_password(
    user_email, domain="demo.django-crm.io", protocol="http"
):
    """ Send Mail To Users When their account is created """
    user = User.objects.filter(email=user_email).first()
    context = {}
    context["user_email"] = user_email
    context["url"] = protocol + "://" + domain
    context["uid"] = (urlsafe_base64_encode(force_bytes(user.pk)),)
    context["token"] = default_token_generator.make_token(user)
    context["token"] = context["token"]
    context["complete_url"] = context[
        "url"
    ] + "/auth/reset-password/{uidb64}/{token}/".format(
        uidb64=context["uid"][0], token=context["token"]
    )
    subject = "Set a New Password"
    recipients = []
    recipients.append(user_email)
    html_content = render_to_string("password_reset_email.html", context=context)
    if recipients:
        msg = EmailMessage(
            subject, html_content, from_email=settings.EMAIL_HOST_USER, to=recipients
        )
        msg.content_subtype = "html"
        msg.send()
