from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    path(
        "",
        views.IndexView.as_view(),
        name="index"
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout"
    ),
    path(
        "registration/",
        views.UserRegisterView.as_view(),
        name="registration"
    ),
    path(
        "profile/edit/",
        views.ProfileEditView.as_view(),
        name="edit_profile"
    ),
    path(
        "account/edit/",
        views.UserEditView.as_view(),
        name="edit_user"
    ),
    path(
        "search/",
        views.SearchView.as_view(),
        name="search"
    ),
    path(
        "user/<str:username>/",
        views.UserProfileView.as_view(),
        name="profile"
    ),
    path(
        "user/<str:username>/follow/",
        views.FollowUserView.as_view(),
        name="follow"
    ),
    path(
        "user/<str:username>/followers/",
        views.FollowersListView.as_view(),
        name="followers"
    ),
    path(
        "user/<str:username>/following/",
        views.FollowingListView.as_view(),
        name="following"
    ),
]