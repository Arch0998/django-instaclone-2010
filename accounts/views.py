from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.views.generic import CreateView, DetailView
from django.shortcuts import get_object_or_404
from accounts.forms import UserRegisterForm
from accounts.models import User


class HomeLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return f"/user/{self.request.user.username}/"
