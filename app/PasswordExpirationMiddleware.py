from django.utils import timezone
from datetime import timedelta
from django.shortcuts import redirect, render
from django.contrib import messages

from PSSSAS_PP_Membership.forms import UserPasswordChangeForm

class PasswordExpirationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_change = request.user.last_password_change
            if last_change and timezone.now() - last_change > timedelta(days=60):
                # if last_change and timezone.now() - last_change > timedelta(minutes=1):
                if request.path != '/accounts/password-change/':  # Adjust this path if necessary
                    messages.warning(request, "Your password is expired! Please change it.")
                    return redirect('password_change')  # Redirect to the password change view

        # Proceed with the request if no redirect occurs
        response = self.get_response(request)
        return response