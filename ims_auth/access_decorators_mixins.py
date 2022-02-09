from functools import wraps

from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


def admin_login_required(function):
    """ this function is a decorator used to authorize if a user is admin """
    def wrap(request, *args, **kwargs):
        if request.user.role == 'ADMIN' or request.user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap