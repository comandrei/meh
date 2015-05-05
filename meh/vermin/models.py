from django.conf import settings
from django.db import models

from .tasks import generate_thumbnail, send_email

THUMBNAIL_SIZES = [
    (120, 120),
    (90, 90)
]


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    image = models.ImageField(upload_to="posts",
                              null=True, blank=True)

    def save(self, *args, **kwargs):
        post = super(Post, self).save(*args, **kwargs)
        if self.image:
            for size in THUMBNAIL_SIZES:
                generate_thumbnail.delay(self.image.path, size)
        return post


class Meh(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)

    def save(self, *args, **kwargs):
        meh = super(Meh, self).save(*args, **kwargs)
        send_email.delay(to=self.post.author.email,
                         from_email=self.author.email,
                         subject="{} mehed your your post {}".format(self.author, self.post),
                         text="trololo")
        return meh


class Eh(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)

    def save(self, *args, **kwargs):
        eh = super(Eh, self).save(*args, **kwargs)
        send_email.delay(to=self.post.author.email,
                         from_email=self.author.email,
                         subject="{} ehed your your post {}".format(self.author, self.post),
                         text="trololololo")
        return eh
