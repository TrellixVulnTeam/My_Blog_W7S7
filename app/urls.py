from django.conf.urls import url
from . import views


urlpattern = [
    url(r'^$', views.index, name='index')
    url(r'^(P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'
        r'(?P<post>[-\w]+)/$', views.post_detail, name='post_detail')
]