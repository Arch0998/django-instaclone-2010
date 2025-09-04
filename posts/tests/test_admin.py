from django.test import TestCase
from django.contrib.admin.sites import AdminSite

from posts.models import Post, Comment, Hashtag, PostLike
from posts.admin import PostAdmin, CommentAdmin, HashtagAdmin, PostLikeAdmin


class TestUsersMixin:
    def setUp(self):
        from accounts.models import User
        self.user = User.objects.create(
            username="postadminuser",
            email="postadminuser@example.com",
            phone="+380987654370"
        )
        self.user2 = User.objects.create(
            username="postadminuser2",
            email="postadminuser2@example.com",
            phone="+380987654371"
        )


class PostAdminTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.site = AdminSite()
        self.post = Post.objects.create(
            author=self.user,
            caption="Test caption for post",
            image="test.jpg"
        )
        self.admin = PostAdmin(Post, self.site)

    def test_list_display(self):
        self.assertIn("author", self.admin.list_display)
        self.assertIn("caption_short", self.admin.list_display)
        self.assertIn("likes_count", self.admin.list_display)

    def test_search_fields(self):
        self.assertIn("author__username", self.admin.search_fields)
        self.assertIn("caption", self.admin.search_fields)

    def test_caption_short(self):
        short = self.admin.caption_short(self.post)
        self.assertTrue(isinstance(short, str))

    def test_likes_count(self):
        self.assertEqual(self.admin.likes_count(self.post), 0)


class CommentAdminTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.site = AdminSite()
        self.post = Post.objects.create(
            author=self.user,
            caption="Test caption",
            image="test.jpg"
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user2,
            content="Test comment content"
        )
        self.admin = CommentAdmin(Comment, self.site)

    def test_list_display(self):
        self.assertIn("author", self.admin.list_display)
        self.assertIn("content_short", self.admin.list_display)

    def test_search_fields(self):
        self.assertIn("author__username", self.admin.search_fields)
        self.assertIn("content", self.admin.search_fields)

    def test_content_short(self):
        short = self.admin.content_short(self.comment)
        self.assertTrue(isinstance(short, str))


class HashtagAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.hashtag = Hashtag.objects.create(name="testtag")
        self.admin = HashtagAdmin(Hashtag, self.site)

    def test_list_display(self):
        self.assertIn("name", self.admin.list_display)
        self.assertIn("posts_count", self.admin.list_display)

    def test_search_fields(self):
        self.assertIn("name", self.admin.search_fields)

    def test_posts_count(self):
        self.assertEqual(self.admin.posts_count(self.hashtag), 0)


class PostLikeAdminTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.site = AdminSite()
        self.post = Post.objects.create(
            author=self.user,
            caption="Test caption",
            image="test.jpg"
        )
        self.postlike = PostLike.objects.create(
            post=self.post,
            user=self.user2
        )
        self.admin = PostLikeAdmin(PostLike, self.site)

    def test_list_display(self):
        self.assertIn("post", self.admin.list_display)
        self.assertIn("user", self.admin.list_display)

    def test_search_fields(self):
        self.assertIn("post__caption", self.admin.search_fields)
        self.assertIn("user__username", self.admin.search_fields)
