from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class structure(models.Model):
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250, unique_for_date='published', null=True)
    content=models.TextField()
    author=models.ForeignKey(User,related_name='blog_post', null=True)
    created=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    published = models.DateTimeField(default=now, )
    updated=models.DateTimeField(auto_now=True, auto_now_add=False)
    STATE_CHOICES = (
        ('pending', 'Pending'),
        ('published', 'Published')

    )
    status = models.CharField(max_length=15, choices=STATE_CHOICES, default='pending')


  #  def get_absolute_url(self):
   #     return reverse('app:post_detail',args=[self.published.year,
    #                                           self.published.strftime('%m'),self.published.strftime('$d'),
     #                                          self.slug])

    class Meta:
        ordering=('published', )


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
