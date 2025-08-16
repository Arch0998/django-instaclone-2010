from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    ),
    image = models.ImageField(
        upload_to="posts/%Y/%m/%d/",
        blank=True
    ),
    caption = models.TextField(
        blank=True
    )
    created_at = models.DateTimeField(
        default=timezone.now
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="PostLike",
        related_name="liked_posts",
        blank=True
    )

    def __str__(self):
        return f"Post #{self.id} by {self.author.username}"

    def clean(self):
        if not self.image and not self.caption:
            raise ValidationError("Post must have an image or a caption.")


class PostLike(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        unique_together = ("user", "post")


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(
        default=timezone.now
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def clean(self):
        if not self.content:
            raise ValidationError("Comment must have a content.")


class Hashtag(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True
    )
    posts = models.ManyToManyField(
        Post,
        related_name="hashtags",
        blank=True
    )

    def __str__(self):
        return f"#{self.name}"
