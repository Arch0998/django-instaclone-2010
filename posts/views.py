from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q

from posts.models import Post, Comment, PostLike
from accounts.models import User


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ["image", "caption"]
    template_name = "posts/create_post.html"
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy(
            "accounts:profile",
            kwargs={'username': self.request.user.username}
        )


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all().order_by("created_at")
        context["is_liked"] = False
        if self.request.user.is_authenticated:
            context["is_liked"] = PostLike.objects.filter(
                user=self.request.user,
                post=self.object
            ).exists()
        return context


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    fields = ["caption"]
    template_name = "posts/edit_post.html"
    
    def get_object(self):
        obj = super().get_object()
        if obj.author != self.request.user:
            messages.error(
                self.request,
                "You can only edit your own posts."
            )
            return redirect('posts:detail', pk=obj.pk)
        return obj
    
    def get_success_url(self):
        messages.success(self.request, "Post updated successfully!")
        return reverse_lazy("posts:detail", kwargs={'pk': self.object.pk})


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    
    def get_object(self):
        obj = super().get_object()
        if obj.author != self.request.user:
            messages.error(
                self.request,
                "You can only delete your own posts."
            )
            return redirect('posts:detail', pk=obj.pk)
        return obj

    def get_success_url(self):
        messages.success(self.request, "Post deleted successfully!")
        return reverse_lazy(
            "accounts:profile",
            kwargs={'username': self.request.user.username}
        )


class AddCommentView(LoginRequiredMixin, generic.View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        content = request.POST.get("content")
        if content:
            Comment.objects.create(
                post=post,
                author=request.user,
                content=content
            )
        return JsonResponse({"success": True})


class DeleteCommentView(LoginRequiredMixin, generic.View):
    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if (comment.author == request.user or comment.post.author == request.user):
            comment.delete()
            return JsonResponse({"success": True})
        return JsonResponse({"success": False, "error": "Permission denied"})


class LikePostView(LoginRequiredMixin, generic.View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like, created = PostLike.objects.get_or_create(
            user=request.user,
            post=post
        )
        
        if not created:
            # Unlike the post
            like.delete()
            is_liked = False
        else:
            is_liked = True
        
        return JsonResponse({
            "success": True,
            "is_liked": is_liked,
            "likes_count": post.likes.count()
        })


class SearchUsersView(LoginRequiredMixin, generic.View):
    def get(self, request):
        query = request.GET.get('q', '').strip()
        users = []

        if query:
            users = User.objects.filter(
                username__icontains=query
            ).exclude(
                id=request.user.id if request.user.is_authenticated else None
            )[:10]
        
        return JsonResponse({
            "users": [
                {
                    "id": user.id,
                    "username": user.username,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "avatar": user.profile.avatar.url if user.profile.avatar else None,
                    "profile_url": reverse_lazy(
                        "accounts:profile", kwargs={"username": user.username}
                    )
                }
                for user in users
            ]
        })
