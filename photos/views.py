from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from photos.models import Post, Comment
from django.urls import reverse

# Create your views here.
def index(request):
    context = {
        'title': 'Latest Photos',
        'posts': Post.objects.order_by("created_at").reverse(),
    }
    return render(request, 'photos/index.html', context)

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post:
        context = {
            'title': 'View Photo',
            'is_authed': False,
            'post': Post.objects.get(id=post_id),
            'comments': Comment.objects.filter(post=post_id),
        }
        return render(request, 'photos/post.html', context)
    else:
        return HttpResponseRedirect(reverse('index'))