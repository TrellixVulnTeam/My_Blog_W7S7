from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class structure(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()
    author=models.ForeignKey(User,related_name='blog_post')
    created=models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now())
    updated=models.DateTimeField(auto_now=True, auto_now_add=False)
    slug=models.SlugField(max_length=250,unique_for_date='published')

    class Meta:
        ordering=("-published")


    def __str__(self):
        return self.title


class comment(models.Model):
    post = models.ForeignKey(structure, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering=('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name,self.post)
