from django.urls import path
from posts import views

app_name = "posts"

urlpatterns = [
    path(
        "create/",
        views.PostCreateView.as_view(),
        name="create"
    ),
    path(
        "<int:pk>/",
        views.PostDetailView.as_view(),
        name="detail"
    ),
    path("<int:pk>/comment/",
         views.AddCommentView.as_view(),
         name="add_comment"
         )
]