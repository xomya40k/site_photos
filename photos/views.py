from django.shortcuts import render
from photos.models import Post

# Create your views here.
def index(request):
    context = {
        'title': 'Latest Photos',
        'posts': Post.objects.order_by("created_at").reverse(),
    }
    return render(request, 'photos/index.html', context)

def post(request):
    context = {
        'title': 'View Photo',
        'is_authed': False,
        'post': {
            'id': '1',
            'author': {
                'id': '1',
                'username': 'user1',
                'image': 'iuCkR.jpg'
            },
            'image': '30b2375593ffa167fc4b8870a40a48b9.jpg',
            'description': 'This is a sample photo',
            'comments': [
                {
                    'id': '1',
                    'author': {
                        'id': '1',
                        'username': 'user1',
                        'image': 'iuCkR.jpg'
                    },
                    'text':'Hello!',
                },
                {
                    'id': '1',
                    'author': {
                        'id': '1',
                        'username': 'user1',
                        'image': 'iuCkR.jpg'
                    },
                    'text':'Hello!',
                },
            ],
        }
    }
    return render(request, 'photos/post.html', context)