from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "registration/",
        views.UserRegisterView.as_view(),
        name="registration"
    ),
    path(
        "password_reset/",
        views.CustomPasswordResetView.as_view(),
        name="password_reset"
    ),
    path(
        "password_reset/done/",
        views.CustomPasswordResetDoneView.as_view(),
        name="password_reset_done"
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm"
    ),
    path(
        "reset/complete/",
        views.CustomPasswordResetCompleteView.as_view(),
        name="password_reset_complete"
    ),
    path(
        "profile/edit/",
        views.ProfileEditView.as_view(),
        name="edit_profile"
    ),
    path(
        "search/", views.SearchView.as_view(), name="search"
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
