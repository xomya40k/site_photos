from django.db import models
from django.contrib.auth.models import User
import uuid
from stdimage import StdImageField
# Create your models here.

def image_path(instance, filename):
    return 'uploads/user_{0}/{1}'.format(instance.author.id, filename)

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    photo = StdImageField(upload_to=image_path, blank=True, variations={'medium': (300, 200), 'thumbnail': (50, 50, True)})
    text = models.TextField(max_length=512)
    likes = models.PositiveIntegerField(default=0, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Поcт: {self.id}, Автор: {self.author.id}'

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=512)
    likes = models.PositiveIntegerField(default=0, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Комментарий: {self.id}, Поcт: {self.post.id}, Автор: {self.author.id}'