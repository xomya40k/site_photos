from django.db import models
from django.contrib.auth.models import AbstractUser
from stdimage import StdImageField
# Create your models here.

def image_path(instance, filename):
    return 'uploads/user_{0}/{1}'.format(instance.id, filename)

class User(AbstractUser):
    photo = StdImageField(upload_to=image_path, blank=True, variations={'medium': (300, 200), 'thumbnail': (50, 50, True)})
    description = models.TextField(max_length=512)
    is_moderator = models.BooleanField(default=False, null=False)