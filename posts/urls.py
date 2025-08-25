from django.urls import path
from posts import views


app_name = "posts"

urlpatterns = [
    path("feed/", views.FeedView.as_view(), name="feed"),
    path("create/", views.PostCreateView.as_view(), name="create"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.PostUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete"),
    path(
        "<int:pk>/comment/",
        views.AddCommentView.as_view(),
        name="add_comment"
    ),
    path(
        "comment/<int:pk>/delete/",
        views.DeleteCommentView.as_view(),
        name="delete_comment",
    ),
    path("<int:pk>/like/", views.LikePostView.as_view(), name="like"),
    path(
        "search-users/",
        views.SearchUsersView.as_view(),
        name="search_users"
    ),
    path(
        "hashtag/<str:hashtag>/",
        views.HashtagPostsView.as_view(),
        name="hashtag_posts"
    ),
]
