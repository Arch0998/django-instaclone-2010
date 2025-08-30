from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.shortcuts import redirect, get_object_or_404, render
from django.http import JsonResponse
from django.views import View
from django.contrib import messages
from django.db.models import Q

from accounts.models import User, Follow, UserProfile
from accounts.forms import UserRegisterForm, UserEditForm, ProfileEditForm


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
        super().form_valid(form)
        UserProfile.objects.get_or_create(user=self.object)

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
        context["posts"] = self.object.posts.order_by("-created_at")
        context["posts_count"] = context["posts"].count()

        if self.request.user.is_authenticated:
            context["is_following"] = Follow.objects.filter(
                follower=self.request.user, following=self.object
            ).exists()
        else:
            context["is_following"] = False

        context["followers_count"] = self.object.followers_set.count()
        context["following_count"] = self.object.following_set.count()

        return context


class ProfileEditView(LoginRequiredMixin, View):
    template_name = "accounts/edit_profile.html"

    def get(self, request):
        user_form = UserEditForm(instance=request.user, user=request.user)
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile_form = ProfileEditForm(instance=profile)

        return render(
            request,
            self.template_name,
            {
                "user_form": user_form,
                "profile_form": profile_form,
                "user": request.user,
            },
        )

    def post(self, request):
        user_form = UserEditForm(
            request.POST,
            instance=request.user,
            user=request.user
        )
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile_form = ProfileEditForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request,
                "Profile updated successfully!"
            )
            return redirect(
                "accounts:profile",
                username=request.user.username
            )

        return render(
            request,
            self.template_name,
            {
                "user_form": user_form,
                "profile_form": profile_form,
                "user": request.user,
            },
        )


class FollowUserView(LoginRequiredMixin, View):
    def post(self, request, username):
        user_to_follow = get_object_or_404(User, username=username)

        if user_to_follow == request.user:
            return JsonResponse(
                {"success": False, "error": "You cannot follow yourself"}
            )

        follow, created = Follow.objects.get_or_create(
            follower=request.user,
            following=user_to_follow
        )

        if not created:
            follow.delete()
            is_following = False
        else:
            is_following = True

        return JsonResponse(
            {
                "success": True,
                "is_following": is_following,
                "followers_count": user_to_follow.followers_set.count(),
            }
        )


class FollowersListView(LoginRequiredMixin, ListView):
    template_name = "accounts/followers.html"
    context_object_name = "followers"
    paginate_by = 20

    def get_queryset(self):
        self.profile_user = get_object_or_404(
            User,
            username=self.kwargs["username"]
        )
        return (Follow.objects.filter(following=self.profile_user)
                .select_related("follower", "follower__profile"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile_user"] = self.profile_user
        context["count"] = self.profile_user.followers_set.count()

        if self.request.user.is_authenticated:
            user_following = Follow.objects.filter(
                follower=self.request.user
            ).values_list("following_id", flat=True)
            context["user_following"] = list(user_following)
        else:
            context["user_following"] = []

        return context


class FollowingListView(LoginRequiredMixin, ListView):
    template_name = "accounts/following.html"
    context_object_name = "following"
    paginate_by = 20

    def get_queryset(self):
        self.profile_user = get_object_or_404(
            User,
            username=self.kwargs["username"]
        )
        return (Follow.objects.filter(follower=self.profile_user)
                .select_related("following", "following__profile"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile_user"] = self.profile_user
        context["count"] = self.profile_user.following_set.count()

        if self.request.user.is_authenticated:
            user_following = Follow.objects.filter(
                follower=self.request.user
            ).values_list("following_id", flat=True)
            context["user_following"] = list(user_following)
        else:
            context["user_following"] = []

        return context


class SearchView(LoginRequiredMixin, ListView):
    template_name = "accounts/search.html"
    context_object_name = "users"
    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get("q", "").strip()
        if query:
            queryset = User.objects.filter(
                Q(username__icontains=query)
                | Q(first_name__icontains=query)
                | Q(last_name__icontains=query)
            )

            if self.request.user.is_authenticated:
                queryset = queryset.exclude(id=self.request.user.id)

            return queryset
        return User.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        return context
