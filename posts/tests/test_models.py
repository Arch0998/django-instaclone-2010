from django.test import TestCase
from django.core.exceptions import ValidationError

from posts.models import Post, PostLike, Comment, Hashtag


class TestUsersMixin:
    def setUp(self):
        from accounts.models import User
        self.user = User.objects.create(
            username="postmodeluser",
            email="postmodeluser@example.com",
            phone="+380987654380"
        )
        self.user2 = User.objects.create(
            username="postmodeluser2",
            email="postmodeluser2@example.com",
            phone="+380987654381"
        )


class PostModelTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.post = Post.objects.create(
            author=self.user,
            caption="Test caption #tag",
            image="test.jpg"
        )

    def test_str(self):
        self.assertIn(self.user.username, str(self.post))

    def test_clean_requires_image(self):
        post = Post(author=self.user, caption="No image")
        with self.assertRaises(ValidationError):
            post.clean()

    def test_hashtags_created(self):
        self.post.save()
        self.assertTrue(
            Hashtag.objects.filter(name="tag", posts=self.post).exists()
        )

    def test_likes_relation(self):
        PostLike.objects.create(post=self.post, user=self.user2)
        self.assertIn(self.user2, self.post.likes.all())


class PostLikeModelTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.post = Post.objects.create(
            author=self.user,
            caption="Like test",
            image="test.jpg"
        )

    def test_unique_like(self):
        PostLike.objects.create(post=self.post, user=self.user2)
        with self.assertRaises(Exception):
            PostLike.objects.create(post=self.post, user=self.user2)


class CommentModelTest(TestUsersMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.post = Post.objects.create(
            author=self.user,
            caption="Comment test",
            image="test.jpg"
        )

    def test_clean_requires_content(self):
        comment = Comment(post=self.post, author=self.user, content="")
        with self.assertRaises(ValidationError):
            comment.clean()

    def test_str(self):
        comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content="Test comment"
        )
        self.assertIn("Test comment", comment.content)


class HashtagModelTest(TestCase):
    def setUp(self):
        self.hashtag = Hashtag.objects.create(name="testtag")

    def test_str(self):
        self.assertEqual(str(self.hashtag), "#testtag")

    def test_posts_relation(self):
        from accounts.models import User
        user = User.objects.create(
            username="hashtaguser",
            email="hashtaguser@example.com",
            phone="+380987654382"
        )
        post = Post.objects.create(
            author=user,
            caption="#testtag",
            image="test.jpg"
        )
        post.hashtags.add(self.hashtag)
        self.assertIn(post, self.hashtag.posts.all())
