from django.test import TestCase, Client
from django.urls import reverse

from posts.models import Post, Comment, PostLike, Hashtag
from accounts.models import User, Follow


class TestUsersMixin:
    def setUp(self):
        self.user = User.objects.create(
            username="postviewuser",
            email="postviewuser@example.com",
            phone="+380987654390"
        )
        self.user2 = User.objects.create(
            username="postviewuser2",
            email="postviewuser2@example.com",
            phone="+380987654391"
        )


class FeedViewTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.client.force_login(self.user)
        Follow.objects.create(follower=self.user, following=self.user2)
        self.post = Post.objects.create(
            author=self.user2,
            caption="Feed test",
            image="https://res.cloudinary.com/demo/image/upload/sample.jpg"
        )

    def test_feed_view(self):
        response = self.client.get(reverse("posts:feed"))
        self.assertEqual(response.status_code, 200)


class PostCreateViewTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.client.force_login(self.user)

    def test_create_post_view_get(self):
        response = self.client.get(reverse("posts:create"))
        self.assertEqual(response.status_code, 200)


class PostDetailViewTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.client.force_login(self.user)
        self.post = Post.objects.create(
            author=self.user,
            caption="Detail test",
            image="https://res.cloudinary.com/demo/image/upload/sample.jpg"
        )

    def test_detail_view(self):
        response = self.client.get(
            reverse("posts:detail", args=[self.post.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Detail test")


class PostUpdateViewTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.client.force_login(self.user)
        self.post = Post.objects.create(
            author=self.user,
            caption="Update test",
            image="https://res.cloudinary.com/demo/image/upload/sample.jpg"
        )

    def test_update_view_get(self):
        response = self.client.get(reverse("posts:edit", args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)


class PostDeleteViewTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.client.force_login(self.user)
        self.post = Post.objects.create(
            author=self.user,
            caption="Delete test",
            image="https://res.cloudinary.com/demo/image/upload/sample.jpg"
        )

    def test_delete_post(self):
        response = self.client.post(
            reverse("posts:delete", args=[self.post.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())


class AddCommentViewTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.client.force_login(self.user)
        self.post = Post.objects.create(
            author=self.user,
            caption="Comment test",
            image="https://res.cloudinary.com/demo/image/upload/sample.jpg"
        )

    def test_add_comment(self):
        url = reverse("posts:add_comment", args=[self.post.pk])
        response = self.client.post(url, {"content": "Test comment"})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Comment.objects.filter(content="Test comment").exists()
        )


class DeleteCommentViewTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.client.force_login(self.user)
        self.post = Post.objects.create(
            author=self.user,
            caption="Comment delete test",
            image="https://res.cloudinary.com/demo/image/upload/sample.jpg"
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content="To delete"
        )

    def test_delete_comment(self):
        url = reverse("posts:delete_comment", args=[self.comment.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Comment.objects.filter(pk=self.comment.pk).exists())


class LikePostViewTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.client.force_login(self.user)
        self.post = Post.objects.create(
            author=self.user2,
            caption="Like test",
            image="https://res.cloudinary.com/demo/image/upload/sample.jpg"
        )

    def test_like_unlike_post(self):
        url = reverse("posts:like", args=[self.post.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            PostLike.objects.filter(post=self.post, user=self.user).exists()
        )
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            PostLike.objects.filter(post=self.post, user=self.user).exists()
        )


class SearchUsersViewTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.client.force_login(self.user)

    def test_search_users(self):
        url = reverse("posts:search_users") + "?q=postviewuser2"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("postviewuser2", response.content.decode())


class HashtagPostsViewTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.client.force_login(self.user)
        self.post = Post.objects.create(
            author=self.user,
            caption="#hashtag test",
            image="https://res.cloudinary.com/demo/image/upload/sample.jpg"
        )
        hashtag, _ = Hashtag.objects.get_or_create(name="hashtag")
        self.post.hashtags.add(hashtag)

    def test_hashtag_posts(self):
        url = reverse("posts:hashtag_posts", args=["hashtag"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
