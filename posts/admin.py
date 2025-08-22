from django.contrib import admin
from posts.models import Post, Comment, Hashtag, PostLike


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "author",
        "caption_short",
        "created_at",
        "likes_count"
    ]
    search_fields = [
        "author__username",
        "caption"
    ]
    list_filter = [
        "created_at",
        "author"
    ]
    readonly_fields = ["created_at", "updated_at"]

    def caption_short(self, obj):
        return obj.caption[:50] + "..." if len(obj.caption) > 50 else obj.caption
    caption_short.short_description = "Caption"

    def likes_count(self, obj):
        return obj.likes.count()
    likes_count.short_description = "Likes"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "author",
        "content_short",
        "created_at"
    ]
    search_fields = [
        "author__username",
        "content"
    ]
    list_filter = [
        "created_at",
        "author"
    ]
    readonly_fields = ["created_at", "updated_at"]

    def content_short(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    content_short.short_description = "Content"


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "posts_count"
    ]
    search_fields = ["name"]

    def posts_count(self, obj):
        return obj.posts.count()
    posts_count.short_description = "Posts with this hashtag"


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "user",
        "created_at"
    ]
    search_fields = [
        "post__caption",
        "user__username"
    ]
    list_filter = [
        "created_at",
        "user"
    ]
    readonly_fields = ["created_at"]
