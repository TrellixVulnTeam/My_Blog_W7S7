from django.shortcuts import render, get_object_or_404
from .models import structure


def index(request):
    posts = structure.published.all()
    return render(request, 'list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(structure, slug=post, status='published',
                             publish_year=year, publish_month=month, publish_day=day)
    return render(request, 'detail.html', {'post': post})

