from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.shortcuts import redirect
from accounts.models import User

from accounts.forms import UserRegisterForm

class IndexView(LoginView):
    template_name = "accounts/index.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return f"/user/{self.request.user.username}/"


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = "accounts/registration.html"
    success_url = reverse_lazy("accounts:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect("accounts:profile", username=user.username)


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "accounts/profile.html"
    context_object_name = "profile_user"
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = self.object.posts.all().order_by("-created_at")
        context["posts_count"] = context["posts"].count()
        return context
