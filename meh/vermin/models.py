from django.conf import settings
from django.db import models

from .utils import generate_thumbnail

THUMBNAIL_SIZES = [
    (120, 120),
    (90, 90)
]


class Post(models.Model):
    author = models.OneToOneField(settings.AUTH_USER_MODEL)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    image = models.ImageField(upload_to="posts",
                              null=True, blank=True)

    def save(self, *args, **kwargs):
        post = super(Post, self).save(*args, **kwargs)
        if self.image:
            for size in THUMBNAIL_SIZES:
                generate_thumbnail(self.image.path, size)
        return post


class Meh(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.OneToOneField(settings.AUTH_USER_MODEL)
    post = models.OneToOneField(Post)


class Eh(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.OneToOneField(settings.AUTH_USER_MODEL)
    post = models.OneToOneField(Post)
