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
        "user/<str:username>/",
        views.UserProfileView.as_view(),
        name="profile"),
]
