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
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
    slug=models.SlugField(max_length=250,unique_for_date='published')

    class Meta:
        ordering=("-published")





    def __str__(self):
        return self.title
