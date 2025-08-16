from django.contrib import admin
from django.contrib.auth.admin import Group, UserAdmin

from accounts.models import User, UserProfile, Follow


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = [
        "username",
        "first_name",
        "last_name",
        "email",
        "phone",
        "is_active",
        "is_staff",
    ]
    search_fields = [
        "username",
        "first_name",
        "last_name",
        "email",
        "phone",
    ]


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = [
        "follower",
        "following"
    ]
    search_fields = [
        "follower__username",
        "following__username"
    ]
    list_filter = [
        "follower",
        "following"
    ]
