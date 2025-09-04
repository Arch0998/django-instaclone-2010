from django.test import SimpleTestCase
from django.urls import reverse, resolve

from posts import views


class PostsUrlsTest(SimpleTestCase):
    def test_feed_url(self):
        url = reverse("posts:feed")
        self.assertEqual(
            resolve(url).func.view_class, views.FeedView
        )

    def test_create_url(self):
        url = reverse("posts:create")
        self.assertEqual(
            resolve(url).func.view_class, views.PostCreateView)

    def test_detail_url(self):
        url = reverse("posts:detail", args=[1])
        self.assertEqual(
            resolve(url).func.view_class, views.PostDetailView)

    def test_edit_url(self):
        url = reverse("posts:edit", args=[1])
        self.assertEqual(
            resolve(url).func.view_class, views.PostUpdateView)

    def test_delete_url(self):
        url = reverse("posts:delete", args=[1])
        self.assertEqual(
            resolve(url).func.view_class, views.PostDeleteView
        )

    def test_add_comment_url(self):
        url = reverse("posts:add_comment", args=[1])
        self.assertEqual(
            resolve(url).func.view_class, views.AddCommentView
        )

    def test_delete_comment_url(self):
        url = reverse("posts:delete_comment", args=[1])
        self.assertEqual(
            resolve(url).func.view_class, views.DeleteCommentView
        )

    def test_like_url(self):
        url = reverse("posts:like", args=[1])
        self.assertEqual(
            resolve(url).func.view_class, views.LikePostView
        )

    def test_search_users_url(self):
        url = reverse("posts:search_users")
        self.assertEqual(
            resolve(url).func.view_class, views.SearchUsersView
        )

    def test_hashtag_posts_url(self):
        url = reverse("posts:hashtag_posts", args=["testtag"])
        self.assertEqual(
            resolve(url).func.view_class, views.HashtagPostsView
        )
