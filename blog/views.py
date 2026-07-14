from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import CommentForm


def index(request):
    posts = Post.objects.filter(
        published_at__lte=timezone.now()
    )

    return render(request, "index.html", {
        "posts": posts,
    })


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.user.is_authenticated:

        if request.method == "POST":
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)

                # FIX: attach comment to post
                comment.post = post

                # attach creator
                comment.creator = request.user

                comment.save()

                return redirect(request.path_info)

        else:
            comment_form = CommentForm()

    else:
        comment_form = None

    return render(request, "blog/post-detail.html", {
        "post": post,
        "comment_form": comment_form,
    })