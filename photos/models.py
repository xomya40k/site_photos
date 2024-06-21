from django.db import models
import uuid
from stdimage import StdImageField
# Create your models here.

def image_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)
    image = StdImageField(upload_to=image_path, blank=True, variations={'medium': (300, 200, True), 'thumbnail': (50, 50, True)})
    created_at = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)
    email = models.EmailField(max_length=128, unique=True, null=False)
    password_hash = models.CharField(max_length=128, null=False)
    username = models.CharField(max_length=32, unique=True, null=False)
    first_name = models.CharField(max_length=32, null=False)
    second_name = models.CharField(max_length=32, null=False)
    admin = models.BooleanField(default=False, null=False)
    moderator = models.BooleanField(default=False, null=False)
    photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)
    about = models.TextField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)
    text = models.TextField(max_length=512)
    likes = models.PositiveIntegerField(default=0, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=512)
    likes = models.PositiveIntegerField(default=0, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)