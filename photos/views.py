from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'title': 'Latest Photos',
        'is_authed': False,
        'posts': [
            {
                'id': '1',
                'image': '30b2375593ffa167fc4b8870a40a48b9.jpg'
            },
            {
                'id': '2',
                'image': 'DglrT5Ew88o.jpg'
            },
            {
                'id': '3',
                'image': 'e4866c83393a0eaeac315dc6a2c1b656.jpg'
            },
            {
                'id': '4',
                'image': 'iuCkR.jpg'
            },
            {
                'id': '5',
                'image': 'sample_eff03ea4835bb5d50ceb533611cd6b3a.jpg',
            },
        ],
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