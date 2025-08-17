from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import CreateView, DetailView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse_lazy

from posts.models import Post, Comment


class PostCreateView(LoginRequiredMixin, CreateView):
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


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all().order_by("created_at")
        return context


class AddCommentView(LoginRequiredMixin, View):
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
