from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    query = request.GET.get('q', '')

    posts = Post.objects.filter(published=True)

    if query:
        posts = posts.filter(title__icontains=query)

    posts = posts.order_by('-created_at')

    return render(request, 'newsletter/home.html', {
        'posts': posts,
        'query': query
    })


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, published=True)

    return render(request, 'newsletter/post_detail.html', {
        'post': post
    })